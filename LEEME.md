# NOBUSHI Player

Web que funciona como app: se abre con un enlace, reproduce los temas de NOBUSHI (play, anterior/siguiente, ±10 s, reordenar, eliminar) y deja guardarlos en el móvil para oírlos sin conexión.

## Publicación

El repositorio se publica con GitHub Pages (*Settings → Pages → Deploy from a branch → main / (root)*). Enlace: `https://TU-USUARIO.github.io/NOMBRE-DEL-REPO/`

## Añadir, cambiar o quitar temas

1. Pon los audios en la carpeta `temas/` (nombre del archivo = nombre del tema, mejor con el formato `NOBUSHI - NOMBRE.mp3`; en pantalla se quita el "NOBUSHI - " porque ya está el logo).
2. Desde la carpeta del proyecto ejecuta `python3 actualizar-lista.py`. Mantiene el orden que ya había, añade los nuevos al final, quita los que ya no existen y apunta el tamaño de cada archivo.
3. Sube los cambios (`git add . && git commit -m "Temas" && git push`).

Qué pasa en el móvil de cada uno al abrir la web:
- **Tema nuevo:** aparece al final de su lista (su orden no se toca).
- **Tema sustituido** (mismo nombre, otro archivo): se actualiza solo; si tenía copia sin conexión, se vuelve a descargar la nueva. Para que lo detecte hace falta haber pasado el paso 2.
- **Tema quitado de `temas/`:** desaparece de su lista.
- Un tema que alguien elimina a mano en su móvil no vuelve a aparecer.

El orden por defecto para quien entra por primera vez es el de `temas/lista.json`.

## Orden personal de cada uno

Cada persona reordena sus temas (arrastrando ≡ o con ▲▼) y el orden queda guardado en la memoria del propio navegador (IndexedDB): sin cuenta ni sesión, y sin afectar a los demás. En **Subir → Volver al orden original** se restablece el orden de la banda.

El orden se pierde si se borran los datos del navegador, se usa otro móvil/navegador o se navega en modo privado. En iPhone, Safari borra los datos de webs que no se usan en 7 días: conviene *Compartir → Añadir a pantalla de inicio*.

## Cómo lo oyen los demás

- Los temas de `temas/` se reproducen **por internet** (no ocupan espacio).
- La nube ☁ de un tema lo guarda en el móvil para oírlo **sin conexión** (pasa a ✓; otra pulsación quita la copia). **Subir → Guardar todos sin conexión** guarda todos (unos 55 MB ahora).
- **Subir → Elegir audio(s) o un ZIP:** el ZIP se descomprime solo. Esos temas se quedan solo en ese móvil.

## Detalles

- Con el repositorio público, cualquiera con el enlace puede oír y descargar los temas.
- Los temas nuevos subidos a `temas/` se detectan con la API pública de GitHub (límite de 60 consultas por hora por conexión); si falla, se usa `lista.json`.
- Para ZIP el navegador debe ser reciente (Chrome/Edge 103+, Safari 16.4+, Firefox 113+).
- La imagen (`logo.png`, iconos) sale del logo de NOBUSHI. La tipografía es la condensada del sistema (Impact si existe, Roboto Condensed en Android).
