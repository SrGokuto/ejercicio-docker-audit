# Ejercicio Docker Audit

## Links de acceso

### [Nginx Proxy Manager](http://adminnpm-inferna.duckdns.org/)
### [API Flask](http://api-inferna.duckdns.org/)
### [Dozzle](http://dozzle-inferna.duckdns.org/)
### [Uptime Kuma](http://kuma-inferna.duckdns.org/)


## Auditoría de seguridad con Bandit

Ejecución:

```bash
bandit -r . -x ./.venv/
```

- **Python:** 3.14.7
- **Run started:** 2026-09-04 19:13:27.719767+00:00

### Tabla de resultados

| # | ID | Tipo | Severidad | Confianza | CWE | Archivo: Línea | Descripción |
|---|----|------|-----------|-----------|-----|----------------|-------------|
| 1 | B105 | hardcoded_password_string | Low | Medium | CWE-259 | app.py:10 | Posible contraseña hardcodeada: `admin_adso_2026_secreto` |
| 2 | B608 | hardcoded_sql_expressions | Medium | Low | CWE-89 | app.py:25 | Posible inyección SQL por construcción de consulta con strings |
| 3 | B311 | blacklist | Low | High | CWE-330 | app.py:30 | Generadores pseudoaleatorios estándar no aptos para criptografía |
| 4 | B201 | flask_debug_true | High | Medium | CWE-94 | app.py:35 | App Flask ejecutada con `debug=True`, expone el debugger de Werkzeug |
| 5 | B104 | hardcoded_bind_all_interfaces | Medium | Medium | CWE-605 | app.py:35 | Posible binding a todas las interfaces (`0.0.0.0`) |
| 6 | B101 | assert_used | Low | High | CWE-703 | test_app.py:7 | Uso de `assert`; el código se elimina al compilar con bytecode optimizado |

### Métricas

- **Total líneas de código escaneadas:** 34
- **Total líneas omitidas (#nosec):** 0

**Total de problemas por severidad:**

| Severidad | Cantidad |
|-----------|----------|
| Undefined | 0 |
| Low | 3 |
| Medium | 2 |
| High | 1 |

**Total de problemas por confianza:**

| Confianza | Cantidad |
|-----------|----------|
| Undefined | 0 |
| Low | 1 |
| Medium | 3 |
| High | 2 |

**Archivos omitidos:** 0

## Auditoría de seguridad con Bandit (segunda ejecución)

- **Python:** 3.14.7
- **Run started:** 2026-09-04 19:57:30.498564+00:00

### Tabla de resultados

| # | ID | Tipo | Severidad | Confianza | CWE | Archivo: Línea | Descripción |
|---|----|------|-----------|-----------|-----|----------------|-------------|
| 1 | B104 | hardcoded_bind_all_interfaces | Medium | Medium | CWE-605 | app.py:56 | Posible binding a todas las interfaces (`0.0.0.0`) |
| 2 | B101 | assert_used | Low | High | CWE-703 | test_app.py:9 | Uso de `assert`; el código se elimina al compilar con bytecode optimizado |
| 3 | B101 | assert_used | Low | High | CWE-703 | test_app.py:10 | Uso de `assert`; el código se elimina al compilar con bytecode optimizado |
| 4 | B101 | assert_used | Low | High | CWE-703 | test_app.py:12 | Uso de `assert`; el código se elimina al compilar con bytecode optimizado |

### Métricas

- **Total líneas de código escaneadas:** 60
- **Total líneas omitidas (#nosec):** 0
- **Total issues omitidos por desactivación (#nosec BXXX):** 0

**Total de problemas por severidad:**

| Severidad | Cantidad |
|-----------|----------|
| Undefined | 0 |
| Low | 3 |
| Medium | 1 |
| High | 0 |

**Total de problemas por confianza:**

| Confianza | Cantidad |
|-----------|----------|
| Undefined | 0 |
| Low | 0 |
| Medium | 1 |
| High | 3 |

**Archivos omitidos:** 0