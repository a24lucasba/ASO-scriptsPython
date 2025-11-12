#!/home/jefe/scripts/miEnv/bin/python3

from subprocess import run
import unicodedata

def eliminar_tildes(texto):
    # Normaliza el texto y elimina los acentos
    texto_sin_tildes = unicodedata.normalize('NFD', texto)
    texto_sin_tildes = ''.join(c for c in texto_sin_tildes if unicodedata.category(c) != 'Mn')
    return texto_sin_tildes

def borrar_usuario(username):
    """Borra un usuario y su directorio home"""
    try:
        # userdel -r borra el usuario y su directorio home
        cmd = f'sudo userdel -r {username}'
        result = run(cmd, shell=True, capture_output=True, text=True)
        
        if result.returncode == 0:
            print(f"✓ Usuario {username} eliminado correctamente")
        else:
            # Si el usuario no existe, no es un error crítico
            if "does not exist" in result.stderr:
                print(f"⚠ Usuario {username} no existe")
            else:
                print(f"✗ Error eliminando {username}: {result.stderr.strip()}")
    except Exception as e:
        print(f"✗ Error eliminando {username}: {e}")

# Leer el CSV y generar los mismos nombres de usuario
csv_file = 'Simulacro/usuarios.csv'
usuarios_a_borrar = []

print("🗑️  Script para borrar usuarios creados")
print("=" * 50)

with open(csv_file, 'r') as fr:
    lineas = fr.readlines()
    
    # Saltar la cabecera (primera línea)
    for l in lineas[1:]:
        ll = l.strip().split(',')
        
        if len(ll) >= 7:  # Verificar que la línea tenga suficientes campos
            nome = eliminar_tildes(ll[2].lower().replace(' ',''))
            ape1 = list(ll[0])[0].lower()
            ape2 = list(ll[1])[0].lower()
            año1 = list(ll[6])[-2]
            año2 = list(ll[6])[-1]
            
            user = f'a24{nome}{ape1}{ape2}{año1}{año2}'
            usuarios_a_borrar.append(user)

print(f"Se encontraron {len(usuarios_a_borrar)} usuarios para eliminar:")
print("-" * 50)

# Mostrar lista de usuarios antes de borrar
for i, user in enumerate(usuarios_a_borrar, 1):
    print(f"{i:2d}. {user}")

print("-" * 50)
respuesta = input("¿Deseas continuar con la eliminación? (s/N): ").lower()

if respuesta in ['s', 'si', 'sí', 'y', 'yes']:
    print("\n🗑️  Iniciando eliminación de usuarios...")
    print("-" * 50)
    
    for user in usuarios_a_borrar:
        borrar_usuario(user)
    
    print("-" * 50)
    print("✅ Proceso de eliminación completado")
    
else:
    print("❌ Operación cancelada")