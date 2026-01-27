#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Clasificador de Temas para Comentarios de Campañas
Personalizable por campaña/producto
"""

import re
from typing import Callable

def create_topic_classifier() -> Callable[[str], str]:
    """
    Retorna una función de clasificación de temas personalizada para campaña Mini Bon Yurt.
    Campaña enfocada en nuevo tamaño mini diseñado para niños pequeños.
    
    Returns:
        function: Función que toma un comentario (str) y retorna un tema (str)
    
    Usage:
        classifier = create_topic_classifier()
        tema = classifier("Mi hijo lo ama, perfecto para su lonchera")
        # tema = 'Experiencia Positiva - Tamaño/Niños'
    """
    
    def classify_topic(comment: str) -> str:
        """
        Clasifica un comentario en un tema específico basado en patrones regex.
        
        Args:
            comment: Texto del comentario a clasificar
            
        Returns:
            str: Nombre del tema asignado
        """
        comment_lower = str(comment).lower()
        
        # CATEGORÍA 1: Interés de Compra / Intención
        if re.search(
            r'\bquiero\b|\bcomprar\b|\besperar\b|\bpapás\b|\bpadres\b|'
            r'voy a|me lo pueden|pedir|conseguir|me gustaría',
            comment_lower
        ):
            return 'Interés de Compra / Intención'
        
        # CATEGORÍA 2: Precio y Accesibilidad
        if re.search(
            r'\bprecio\b|\bbarato\b|\bplata\b|\bdinero\b|\bcaro\b|'
            r'valor|cuesta|económico|accesible|no hay plata',
            comment_lower
        ):
            return 'Precio y Accesibilidad'
        
        # CATEGORÍA 3: Tamaño y Contenido del Producto
        if re.search(
            r'\bmini\b|\bpequeño\b|\btamaño\b|\bcontenido\b|'
            r'porción|cantidad|poquito|tristeza|repite|repetiría',
            comment_lower
        ):
            return 'Tamaño y Contenido del Producto'
        
        # CATEGORÍA 4: Experiencia Positiva - Tamaño/Niños
        if re.search(
            r'\brico\b|\bbueno\b|\bgusta\b|\bperfecto\b|\bniños\b|'
            r'hijo|hija|pequeños|ideal para|encanta|delicioso',
            comment_lower
        ):
            return 'Experiencia Positiva - Tamaño/Niños'
        
        # CATEGORÍA 5: Opinión sobre la Marca Alpina
        if re.search(
            r'\balpina\b.*\bmejor\b|\balpina\b.*\bproducción\b|'
            r'calidad alpina|confianza en alpina',
            comment_lower
        ):
            return 'Opinión sobre la Marca Alpina'
        
        # CATEGORÍA 6: Salud y Preocupaciones
        if re.search(
            r'gastritis|remedio|enfermedad|estómago|lactosa|'
            r'saludable|malestar|problemas',
            comment_lower
        ):
            return 'Salud y Preocupaciones'
        
        # CATEGORÍA 7: Spam Religioso
        if re.search(
            r'\bam[eé]n\b|\bjesús\b|\bpadre\b.*\bcelestial\b|'
            r'bendiciones|padre mio|dios|señor|oración|rosario',
            comment_lower
        ):
            return 'Spam Religioso'
        
        # CATEGORÍA 8: Solicitudes de Continuación
        if re.search(
            r'\bparte\s*2\b|\bparte\s*dos\b|\bsiguiente\b.*\bparte\b|'
            r'continúa|continuación',
            comment_lower
        ):
            return 'Solicitudes de Continuación'
        
        # CATEGORÍA 9: Fuera de Tema / No Relevante
        if re.search(
            r'jajaja|jeje|sicarios|guerrilla|whatsapp|rata|'
            r'veedores|mirla|talento|hermoso|linda|guap[oa]|'
            r'ojo|correcto|total|así es',
            comment_lower
        ) or len(comment_lower.split()) < 3:
            return 'Fuera de Tema / No Relevante'
        
        # CATEGORÍA DEFAULT: Otros
        return 'Otros'
    
    return classify_topic
# ============================================================================
# METADATA DE LA CAMPAÑA (OPCIONAL)
# ============================================================================

CAMPAIGN_METADATA = {
    'campaign_name': 'Alpina - Kéfir',
    'product': 'Kéfir Alpina',
    'categories': [
        'Preguntas sobre el Producto',
        'Comparación con Kéfir Casero/Artesanal',
        'Ingredientes y Salud',
        'Competencia y Disponibilidad',
        'Opinión General del Producto',
        'Fuera de Tema / No Relevante',
        'Otros'
    ],
    'version': '1.0',
    'last_updated': '2025-11-20'
}


def get_campaign_metadata() -> dict:
    """Retorna metadata de la campaña"""
    return CAMPAIGN_METADATA.copy()
