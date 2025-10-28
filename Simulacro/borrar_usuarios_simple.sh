#!/bin/bash

# Script simple para borrar usuarios del simulacro
# Uso: ./borrar_usuarios_simple.sh

echo "🗑️  Borrando usuarios del simulacro..."
echo "=================================="

# Lista de usuarios basada en el patrón a24*
usuarios_simulacro=$(cut -d: -f1 /etc/passwd | grep "^a24")

if [ -z "$usuarios_simulacro" ]; then
    echo "❌ No se encontraron usuarios con patrón 'a24*'"
    exit 1
fi

echo "Usuarios encontrados:"
echo "$usuarios_simulacro"
echo "=================================="

read -p "¿Deseas eliminar estos usuarios? (s/N): " respuesta

case $respuesta in
    [sS]|[sS][iI]|[yY]|[yY][eE][sS])
        echo "🗑️  Eliminando usuarios..."
        for usuario in $usuarios_simulacro; do
            echo "Eliminando $usuario..."
            sudo userdel -r "$usuario" 2>/dev/null
            if [ $? -eq 0 ]; then
                echo "✓ $usuario eliminado"
            else
                echo "⚠ Error eliminando $usuario (puede que no exista)"
            fi
        done
        echo "✅ Proceso completado"
        ;;
    *)
        echo "❌ Operación cancelada"
        ;;
esac