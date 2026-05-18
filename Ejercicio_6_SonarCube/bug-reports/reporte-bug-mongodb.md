# Reporte de Bug — MongoDB Connection Error

**Proyecto:** SteamLink  
**Fecha:** Mayo 2026  
**Estado:** ✅ Resuelto

---

## Descripción del Problema

La aplicación Node.js fallaba al iniciar, incapaz de conectarse a la base de datos MongoDB Atlas, crasheando el servidor inmediatamente después de arrancar.

## Error

```
querySrv ECONNREFUSED _mongodb._tcp.steamlink.mkloiwz.mongodb.net
    at QueryReqWrap.onresolve [as oncomplete] (node:internal/dns/promises:294:17) {
  errno: undefined,
  code: 'ECONNREFUSED',
  syscall: 'querySrv',
  hostname: '_mongodb._tcp.steamlink.mkloiwz.mongodb.net'
}
```

## Entorno

| Campo        | Detalle                        |
|--------------|-------------------------------|
| Runtime      | Node.js v24.15.0               |
| Framework    | Express + Mongoose             |
| Base de datos| MongoDB Atlas (M0 Free Tier)   |
| OS           | Windows (Git Bash / MINGW64)   |
| Herramienta  | Nodemon 3.0.1                  |

---

## Proceso de Diagnóstico

### Hipótesis 1 — `dotenv` cargaba tarde ❌

`DB_URL` podría ser `undefined` al momento de conectar porque `dotenv` se importaba después de `connectDatabase`.

**Resultado:** Se corrigió el orden de imports, pero el error persistió.

```javascript
// ❌ Antes — dotenv cargaba tarde
const connectDatabase = require("./db/Database.js");
if (process.env.NODE_ENV !== "PRODUCTION") {
  require("dotenv").config({ path: "./config/.env" });
}

// ✅ Después — dotenv primero
if (process.env.NODE_ENV !== "PRODUCTION") {
  require("dotenv").config({ path: "./config/.env" });
}
const connectDatabase = require("./db/Database.js");
```

---

### Hipótesis 2 — IP no estaba en whitelist de Atlas ❌

Atlas rechaza conexiones de IPs no autorizadas.

**Resultado:** La entrada `0.0.0.0/0` ya estaba activa en Network Access. Descartado.

---

### Hipótesis 3 — Contraseña incorrecta en el usuario de Atlas ❌

El usuario `admin` podría no tener la contraseña correcta configurada.

**Resultado:** Se verificó en Database Access y era correcta. Descartado.

---

### Hipótesis 4 — Puerto 27017 bloqueado por la red ❌

Redes universitarias o corporativas frecuentemente bloquean puertos no estándar.

**Resultado:** El SRV lookup con `nslookup` funcionó correctamente desde el sistema, lo que descartó un bloqueo total de red.

```
_mongodb._tcp.steamlink.mkloiwz.mongodb.net  SRV  ac-0iequm1-shard-00-00.mkloiwz.mongodb.net:27017
_mongodb._tcp.steamlink.mkloiwz.mongodb.net  SRV  ac-0iequm1-shard-00-01.mkloiwz.mongodb.net:27017
_mongodb._tcp.steamlink.mkloiwz.mongodb.net  SRV  ac-0iequm1-shard-00-02.mkloiwz.mongodb.net:27017
```

---

### Hipótesis 5 — DNS resolver de Node.js diferente al del sistema ✅

`nslookup` usa la pila DNS del sistema operativo y resolvía correctamente. Sin embargo, Node.js usaba internamente el DNS del router (`192.168.80.1`), el cual no era capaz de resolver registros SRV del protocolo `mongodb+srv://`.

**Resultado:** Causa raíz confirmada.

---

## Causa Raíz

El DNS por defecto del router (`192.168.80.1`) no resolvía correctamente los registros **SRV** usados por el protocolo `mongodb+srv://` en el contexto del resolver interno de Node.js, aunque `nslookup` (que usa la pila DNS del sistema operativo) sí los resolvía sin problema.

Esto produjo un `ECONNREFUSED` en la fase de `querySrv`, antes incluso de intentar la conexión TCP a MongoDB.

---

## Solución Aplicada

Se forzó a Node.js a usar los servidores DNS de Google (`8.8.8.8`) agregando las siguientes líneas al inicio de `server.js`, antes de cualquier otro import:

```javascript
const dns = require('dns');
dns.setDefaultResultOrder('ipv4first');
dns.setServers(['8.8.8.8', '8.8.4.4']);

if (process.env.NODE_ENV !== "PRODUCTION") {
  require("dotenv").config({ path: "./config/.env" });
}
// ... resto del código
```

### Resultado tras el fix

```
Server is running on port 3001
MongoDB connected: ac-0iequm1-shard-00-00.mkloiwz.mongodb.net ✅
```

---

## Notas Adicionales

- En entornos de producción (Render, Railway, Heroku) este fix no es necesario, ya que los servidores cloud tienen DNS confiable. Sin embargo, dejarlo no causa ningún efecto negativo.
- Durante el diagnóstico también se corrigió un typo menor: `useUnifiedTopoLogy` → `useUnifiedTopology` (aunque fue irrelevante para el error principal).
- Las opciones `useNewUrlParser` y `useUnifiedTopology` fueron eliminadas por estar deprecadas en Mongoose 6+.
