﻿# hotel_promo
Hotel promo es una prueba realizada para un puesto de "Full Stack" que permite registrar usuarios para un sorteo especial de San Valentín. La aplicación incluye un sistema de administración que permite generar un ganador y enviarle un correo de notificación. Este proyecto utiliza **Django** para el backend y **Vue.js** para el frontend.

## Características
- Registro de usuarios con validación de correo electrónico.
- Login de administrador con autenticación mediante JWT.
- Panel de administración para generar un ganador del sorteo.
- Seguridad implementada en las rutas protegidas.
- Envío de correos para notificar al ganador.
- Sistema escalable para manejar una cantidad masiva de usuarios.

---

## Tecnologías Utilizadas

### Backend
- **Django**
- **Django Rest Framework (DRF)**
- **Django SimpleJWT** para autenticación
- **Django CORS Headers** para comunicación con el frontend
- **Celery y Redis** (opcional, para manejar tareas asíncronas en producción)

### Frontend
- **Vue.js**
- **Vue Router** para manejo de rutas
- **Axios** para solicitudes HTTP

---

## Requisitos Previos

1. **Python 3.9+**
2. **Node.js 14+** y **npm** o **yarn**
3. **Redis** (opcional, para manejar tareas asíncronas con Celery)
4. Editor de código (por ejemplo, Visual Studio Code)

---

Backend
| Método     | Endpoint     | Descripción     |
|---------------|---------------|---------------|
| POST | /api/register/ | Registro de usuarios |
| POST | /api/verify-email/ | Verificación de correo |
| POST | /api/admin-login/ | Inicio de sesión del administrador |
| POST | /api/generate-winner/ | Generación de ganador y envío de correo |

---

Frontend

| Ruta     | Descripción     | 
|---------------|---------------|
| / | Página de registro de usuario |
| /admin-login| Página de inicio de sesión para admin |
| /admin-panel | Panel protegido para generar ganador |
|  /verify-email| Verificar correo y cambiar contraseña |

