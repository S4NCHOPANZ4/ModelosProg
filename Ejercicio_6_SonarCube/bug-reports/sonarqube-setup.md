# Guía SonarQube — SteamLink (React TS + Node.js)

**Stack:** React TypeScript (frontend) + Node.js (backend)  
**Modo:** Docker local  
**SonarQube version:** 26.5.0

---

## Requisitos previos

- Docker instalado y corriendo
- Node.js instalado
- `sonarqube-scanner` instalado globalmente:

```bash
npm install -g sonarqube-scanner
```

---

## Paso 1 — Levantar SonarQube con Docker

```bash
docker run -d \
  --name sonarqube \
  -p 9000:9000 \
  sonarqube:latest
```

Espera ~1 minuto y entra a **http://localhost:9000**

| Campo      | Valor   |
|------------|---------|
| Usuario    | `admin` |
| Contraseña | `admin` (te pedirá cambiarla al entrar) |

---

## Paso 2 — Crear los proyectos en SonarQube

1. En el dashboard click **Create Project** → **Manually**
2. Crear dos proyectos:
   - Project Key: `steamlink-frontend`
   - Project Key: `steamlink-backend`
3. En cada proyecto, generar un **token de análisis** y guardarlo

---

## Paso 3 — Generar token global (recomendado)

1. Click en tu avatar (arriba a la derecha) → **My Account**
2. Pestaña **Security**
3. En **Generate Token**:
   - Name: `steamlink-token`
   - Type: **Global Analysis Token**
   - Expiration: **No expiration**
4. Click **Generate** → copiar el token (solo se muestra una vez)

> El token tiene el formato: `squ_XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX`  
> Un solo token Global sirve para ambos proyectos.

---

## Paso 4 — Configurar el Backend (Node.js)

Crear el archivo `sonar-project.properties` en la raíz del backend (`/server`):

```properties
sonar.projectKey=steamlink-backend
sonar.projectName=SteamLink Backend
sonar.projectVersion=1.0

sonar.sources=.
sonar.exclusions=**/node_modules/**,**/coverage/**,**/*.test.js
sonar.tests=.
sonar.test.inclusions=**/*.test.js

sonar.javascript.lcov.reportPaths=coverage/lcov.info

sonar.host.url=http://localhost:9000
sonar.token=squ_XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
```

Agregar el script en `server/package.json`:

```json
"scripts": {
  "sonar": "sonar-scanner"
}
```

---

## Paso 5 — Configurar el Frontend (React TS)

Crear el archivo `sonar-project.properties` en la raíz del frontend (`/client`):

```properties
sonar.projectKey=steamlink-frontend
sonar.projectName=SteamLink Frontend
sonar.projectVersion=1.0

sonar.sources=src
sonar.exclusions=**/node_modules/**,**/dist/**,**/*.test.tsx,**/*.test.ts
sonar.tests=src
sonar.test.inclusions=**/*.test.tsx,**/*.test.ts

sonar.typescript.lcov.reportPaths=coverage/lcov.info
sonar.javascript.lcov.reportPaths=coverage/lcov.info

sonar.host.url=http://localhost:9000
sonar.token=squ_XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
```

Agregar el script en `client/package.json`:

```json
"scripts": {
  "sonar": "sonar-scanner"
}
```

---

## Paso 6 — Correr el análisis

```bash
# Backend
cd server
npm run sonar

# Frontend
cd ../client
npm run sonar
```

Debes ver `EXECUTION SUCCESS` en ambos. Luego entra a **http://localhost:9000** para ver los resultados.

---

## Paso 7 — Cerrar Docker correctamente

```bash
docker stop sonarqube
```

Los datos, proyectos y tokens quedan guardados. **No uses `docker rm`** a menos que quieras borrar todo.

---

## Uso diario

| Acción | Comando |
|---|---|
| Arrancar SonarQube | `docker start sonarqube` |
| Parar SonarQube | `docker stop sonarqube` |
| Ver si está corriendo | `docker ps` |
| Ver logs si algo falla | `docker logs sonarqube` |
| Correr análisis backend | `cd server && npm run sonar` |
| Correr análisis frontend | `cd client && npm run sonar` |

Dashboard siempre en: **http://localhost:9000**

---

## Estructura de archivos esperada

```
SteamLink/
├── client/                        ← React TS
│   ├── src/
│   ├── sonar-project.properties   ✅
│   └── package.json
└── server/                        ← Node.js
    ├── sonar-project.properties   ✅
    └── package.json
```

---

## Errores comunes

| Error | Causa | Solución |
|---|---|---|
| `401 Unauthorized` | Token incorrecto o vacío | Regenerar token en My Account → Security |
| `Connection refused` | SonarQube no está corriendo | `docker start sonarqube` y esperar 1 min |
| `Project not found` | `sonar.projectKey` no coincide | Verificar que el key en Atlas y en el `.properties` sean iguales |
