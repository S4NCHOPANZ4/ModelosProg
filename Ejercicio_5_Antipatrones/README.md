# Spooky Month Bot

Bot de Twitter que tuitea diariamente cuántos días faltan para octubr y genera una barra de progreso visual y la publica como imagen. Durante octubre, celebra cada día del mes.
---
## Requisitos
 
- Una cuenta de Twitter-devs con acceso a la API (nivel Basic o superior)
- Credenciales de la API: `consumer_key`, `consumer_secret`, `access_token`, `access_token_secret`, `bearer_token`
---

## Antipatrones

| # | Nombre canónico | Descripción en el proyecto | Dónde |
|---|----------------|---------------------------|-------|
| 1 | **Dead Code** | Funciones y llamadas comentadas (`like_tweet`, `post_tweet_with_image(...)`) que ya no se usan pero siguen en el código. | `main.py:100-110` |
| 2 | **Lava Flow** | Código de pruebas (`test.py`) que quedó mezclado con producción, con lógica duplicada y divergente que nadie se atreve a eliminar. | `test.py` completo |
| 3 | **Magic Numbers** | Números literales sin nombre ni explicación: `240` (segundos de espera), `365` (días del año), `700`/`80` (dimensiones de imagen). | `main.py:88`, `main.py:19`, `main.py:29` |
| 4 | **Copy-Paste Programming** | `create_loading_bar` e `is_it_spookymonth` duplicadas literalmente entre `main.py` y `test.py` con pequeñas diferencias que generan bugs distintos. | `main.py` / `test.py` |
| 5 | **Error Hiding** (Swallowing Exceptions) | `except Exception as e` captura cualquier fallo y solo imprime el error, ocultando problemas fatales y haciendo que el bot siga corriendo indefinidamente. | `main.py:93-95` |
| 6 | **Misleading Name** | La función `tweet_daily` ejecuta cada 4 minutos, no diariamente. El nombre comunica un comportamiento completamente distinto al real. | `main.py:82` |
| 7 | **Async Misuse** (Inappropriate Use of Async) | `create_loading_bar` y `post_tweet_with_image` son declaradas `async` pero solo contienen operaciones síncronas, bloqueando el event loop sin ningún beneficio. | `main.py:29`, `main.py:65` |
| 8 | **Stale Cache / Frozen State** | El estado de `spookyMonth` se calcula una vez al arrancar y nunca se actualiza dentro del loop, haciendo que el bot siempre publique con datos del momento de inicio. | `main.py:83` |
| 9 | **Missing Dependency Declaration** | `Pillow`, la dependencia más importante del proyecto, no está declarada en `requirements.txt`. Cualquier instalación limpia fallará. | `requirements.txt` |
| 10 | **Null Check Omission** | Las variables de entorno se leen con `os.getenv()` sin validar si son `None`. El fallo aparece tarde, con un mensaje de error confuso de Tweepy. | `main.py:13-17` |