# Instrucciones básicas

#### Prompt inicial

```
Crea la estructura básica para un módulo personalizado de "Gestión de solicitudes" para Odoo 19 que permita registrar y gestionar las las solicitudes internas de (IT, RRHH, compras). El stack utilizado es Odoo 19 y PostgreSQL 16.13.
```
```
copia este modulo en la siguiente ubicación: "odoo@192.168.1.73:/opt/odoo/odoo/custom_addons", la clave de acceso es "1234"  
  ```

```
/opt/odoo/odoo/odoo-bin -c /etc/odoo/odoo.conf -i gestion_solicitudes -d odoo19 --stop-after-init
```

Analiza mi estructura de carpetas actual en el explorador de VS Code y, basándote en ella, dime qué nombres exactos deberían tener mis dos repositorios en GitHub 
Quiero organizar mi proyecto de Odoo usando Git Submodules, pero aún no he creado nada en GitHub. Mi módulo local se llama gestion_solicitudes.
Por favor, actúa como un tutor y guíame paso a paso:
Dime exactamente qué dos repositorios debo crear en mi cuenta de GitHub ahora mismo.
Una vez creados, ayúdame con los comandos para convertir mi carpeta gestion_solicitudes en un repositorio independiente y subirlo.
Después, guíame para vincularlo como un submodule dentro de mi proyecto principal, configurando el archivo .gitmodules y el .gitignore de forma automática mediante comandos.
No ejecutes todo de golpe, primero dime qué pasos de configuración previa debo hacer en la web de GitHub 