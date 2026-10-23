# Subí tu especificación con un pull request

Es opcional. Sirve para dos cosas: que otra persona verifique tus casos y que pierdas el miedo a Git. Acá se puede romper: lo peor que pasa es que tu PR no se acepta.

Necesitás una cuenta en [GitHub](https://github.com/signup). Es sin costo.

## Camino A · Desde el navegador (sin instalar nada)

1. Entrá a [github.com/gmaron/educacion-it](https://github.com/gmaron/educacion-it) y tocá **Fork** (arriba a la derecha) y después **Create fork**. Ahora tenés una copia en tu cuenta.
2. En tu fork, entrá a la carpeta `alumnos/`, tocá **Add file → Create new file** y escribí como nombre `<tu-usuario>/especificacion.md`. La barra crea la carpeta.
3. Pegá tu especificación (la plantilla está en [`plantilla-especificacion.md`](plantilla-especificacion.md)) y tocá **Commit changes**.
4. Abrí `alumnos/README.md`, tocá el lápiz y agregá tu línea al final de la tabla. **Commit changes**.
5. Volvé a la página principal de tu fork y tocá **Contribute → Open pull request**. Completá el checklist y tocá **Create pull request**.

## Camino B · Desde la terminal (para jugar con Git)

```bash
git clone https://github.com/<tu-usuario>/educacion-it.git
cd educacion-it
git checkout -b especificacion-divisor
mkdir -p alumnos/<tu-usuario>
cp sabado-1/plantilla-especificacion.md alumnos/<tu-usuario>/especificacion.md
# completá la especificación y agregá tu línea en alumnos/README.md
git add alumnos/
git commit -m "Especificación del divisor de <tu-usuario>"
git push -u origin especificacion-divisor
```

Después abrí el PR desde la página de tu fork. También podés pedírselo a un agente o a la IA: "abrí un PR de esta branch hacia gmaron/educacion-it". Pero leé qué comandos corre antes de aceptarlos.

## Revisá el PR de otra persona

1. Entrá a la pestaña [Pull requests](https://github.com/gmaron/educacion-it/pulls) y elegí uno que no tenga revisión.
2. En **Files changed**, leé su especificación.
3. Elegí 2 casos, calculá el resultado sin preguntar y dejalo como comentario. Si te da otro número, decile cuál: ese caso es ambiguo.

## Para romper con intención

Si querés aprender Git de verdad, probá esto en tu fork:

- **Un conflicto.** Editá `alumnos/README.md` en dos branches distintas, en la misma línea, y mergealas. Resolvé el conflicto a mano.
- **Volver atrás.** Hacé un commit que borre tu especificación y deshacelo con `git revert`.
- **Mantener tu fork al día.** Cuando el repo original tenga cambios, tocá **Sync fork** en GitHub, o con la terminal:

  ```bash
  git remote add upstream https://github.com/gmaron/educacion-it.git
  git pull upstream main
  ```

- **Leer la historia.** `git log --oneline --graph` muestra quién cambió qué y cuándo.

Si algo se rompe y no sabés cómo arreglarlo, borrá el fork y hacé uno nuevo. También vale.
