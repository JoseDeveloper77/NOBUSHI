# Banda Player — publicar y compartir

Web que funciona como app: se abre con un enlace, reproduce los temas de la banda (play, anterior/siguiente, ±10 s, reordenar, eliminar) y deja guardarlos en el móvil para oírlos sin conexión.

Ya incluye 6 temas en la carpeta `temas/` (NOBUSHI: Nuestro rito, Peleando en la oscuridad, Subnormal, Deberían pedir perdón, Cuando pase la tormenta, Les da igual). El orden inicial de la lista es el de `temas/lista.json`.

## 1. Publicarla en GitHub (una sola vez)

### Opción A — con git (como el portafolio)

```
unzip banda-player.zip
cd band-player
git init
git add .
git commit -m "Banda Player"
git branch -M main
git remote add origin https://github.com/TU-USUARIO/NOMBRE-DEL-REPO.git
git push -u origin main
```
(Antes crea en github.com un repositorio **público** vacío con ese nombre.)

### Opción B — sin git, desde la web de GitHub (en ordenador)

Descomprime el ZIP, crea el repositorio público, pulsa *uploading an existing file* y arrastra **todo el contenido de la carpeta** (incluida la carpeta `temas`).

### Opción C — dentro de tu portafolio

Copia la carpeta como `banda/` en el repositorio del portafolio y haz commit + push. Si el portafolio se construye con Vite, Next, React…, ponla dentro de `public/banda/` para que se publique tal cual.

### Activar GitHub Pages

*Settings → Pages → Build and deployment → Deploy from a branch → main / (root) → Save*. En 1–2 minutos estará en:

- Repositorio propio: `https://TU-USUARIO.github.io/NOMBRE-DEL-REPO/`
- Dentro del portafolio: `https://TU-USUARIO.github.io/NOMBRE-PORTAFOLIO/banda/` (o `https://TU-USUARIO.github.io/banda/` si el portafolio es tu sitio personal)

Manda ese enlace por WhatsApp.

## 2. Añadir más temas para toda la banda

Sube los audios (mp3, m4a, wav…) a la carpeta `temas/` del repositorio (*Add file → Upload files*; hasta 25 MB por archivo desde la web). El nombre del archivo es el nombre del tema. Aparecen solos al abrir la app, o al momento con **Subir → Buscar temas nuevos**.

## 3. Cómo lo oyen los demás

- Los temas de `temas/` se reproducen **por internet** (no ocupan espacio).
- Pulsa la nube ☁ de un tema para guardarlo en el móvil y oírlo **sin conexión** (pasa a ✓; pulsa otra vez para quitar la copia). **Subir → Guardar todos sin conexión** los guarda todos (unos 50 MB ahora).
- Cada uno ordena la lista a su gusto sin afectar a los demás.

## 4. Subir un ZIP

En **Subir → Elegir audio(s) o un ZIP** se descomprime solo y añade todos los audios que tenga. Esos temas quedan guardados **solo en ese móvil**; para que los oiga toda la banda hay que ponerlos en `temas/` del repositorio.

## Detalles a tener en cuenta

- GitHub Pages gratis exige repositorio público: cualquiera con el enlace puede oír y descargar los temas.
- Si cambias o renombras un archivo de `temas/`, actualiza también `temas/lista.json`. Si sustituyes un archivo manteniendo el nombre, las copias sin conexión ya guardadas no se actualizan: usa un nombre nuevo.
- La detección automática de temas nuevos usa la API pública de GitHub (límite de 60 consultas por hora por conexión); si falla, la app sigue mostrando los de `lista.json`.
- Para ZIP el navegador debe ser reciente (Chrome/Edge 103+, Safari 16.4+, Firefox 113+).
