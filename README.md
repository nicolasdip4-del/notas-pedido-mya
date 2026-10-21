# Notas de pedido MyA

Formulario para cargar las notas de pedido de **crédito de terreno** (cuota semanal, quincenal o mensual) y **crédito personal**, y generarlas calcadas del talonario de papel en **PDF** o **imagen PNG A4 (300 dpi)**.

**Abrir:** https://nicolasdip4-del.github.io/notas-pedido-mya/

- Funciona en celular y compu, sin instalar nada y sin internet una vez abierto.
- El borrador y las notas impresas se guardan solo en el navegador de cada vendedor (no se envían a ningún servidor).

## Desarrollo

`notas-pedido-mya.html` es un solo archivo generado: no editarlo a mano. Editar `src/notas.html` y correr:

```
python3 build.py
```

Embebe el logo, las fuentes Gotham y `src/vendor/html2canvas.min.js` (html2canvas 1.4.1, MIT).
