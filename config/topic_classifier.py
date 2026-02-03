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
        
        # CATEGORÍA 1: Quejas sobre AZÚCAR y SALUD (NUEVA - MUY FRECUENTE)
        if re.search(
            r'\bazúcar\b|\bazucar\b|\bveneno\b|\bdañino\b|\bdiabetes\b|'
            r'obesidad|hipertensión|calorías vacías|no.*saludable|'
            r'nada saludable|pura saturación|azúcares refinadas|'
            r'guacala|malo para.*salud|publicidad engañosa',
            comment_lower
        ):
            return 'Críticas - Azúcar/No Saludable'
        
        # CATEGORÍA 2: Quejas sobre CANTIDAD DE CEREAL (NUEVA - MUY FRECUENTE)
        if re.search(
            r'mera miseria.*cereal|poquito.*cereal|más cereal|'
            r'poner.*cereal|cereales.*chocolate|choco crispis|'
            r'zucaritas|no trae nada|como.*8 cereales|6 froot|'
            r'casi no tiene.*cereal|tan poquito cereal',
            comment_lower
        ):
            return 'Quejas - Poca Cantidad de Cereal'
        
        # CATEGORÍA 3: PRECIO EXCESIVO (Mejorada - muy común)
        if re.search(
            r'\bcaro\b|\bcarisimo\b|\bcarísimo\b|\brobo\b|'
            r'a.*4500|a.*5000|a.*3000|tan caro|muy caro|'
            r'sale más barato|más barato.*mil|'
            r'mejor.*frutas|compro.*fruta|me sobra|'
            r'costoso|alto.*precio|bien caro|por.*poquito',
            comment_lower
        ):
            return 'Críticas - Precio Excesivo'
        
        # CATEGORÍA 4: Tamaño DEMASIADO PEQUEÑO (Mejorada)
        if re.search(
            r'\bmini\b.*\bpero\b|\bpoquito\b|\bpoquísimo\b|'
            r'tan poquito|muy pequeño|casi nada|suspiro|'
            r'tres cucharas|un bocado|sorbo|muestra|'
            r'quedo.*hambre|quedó.*hambre|no.*suficiente|'
            r'juguete|no me lleno|mini bocado',
            comment_lower
        ):
            return 'Críticas - Tamaño Muy Pequeño'
        
        # CATEGORÍA 5: Solicitud de tamaño MÁS GRANDE (NUEVA)
        if re.search(
            r'lo quiero grande|litro.*yurt|maxi|más grande|'
            r'tamaño grande|un grande|versión grande|'
            r'por.*no.*grande|cuando.*grande',
            comment_lower
        ):
            return 'Solicitud - Tamaño Más Grande'
        
        # CATEGORÍA 6: Comparación con ALQUERÍA (NUEVA - competencia)
        if re.search(
            r'\balquería\b|\balquemix\b|alque|la marca.*alquería',
            comment_lower
        ):
            return 'Mención - Competencia Alquería'
        
        # CATEGORÍA 7: Preferencia por FRUTAS NATURALES (NUEVA)
        if re.search(
            r'mejor.*frutas|frutas naturales|frutas y verduras|'
            r'más barato.*algo saludable|manzana|fruta.*sobra|'
            r'yogurt griego.*manzana',
            comment_lower
        ):
            return 'Preferencia - Frutas Naturales'
        
        # CATEGORÍA 8: Problemas de PRODUCTO (NUEVA - importante)
        if re.search(
            r'vencido|vencidos|estaban.*viejas|ya.*viejas|'
            r'feas|mal estado|calidad',
            comment_lower
        ):
            return 'Quejas - Producto Vencido/Calidad'
        
        # CATEGORÍA 9: Solicitudes de OTROS CEREALES (NUEVA)
        if re.search(
            r'con.*chocolate|choco crispis|cereales.*chocolate|'
            r'con.*otros cereales|zucaritas|granola|'
            r'cereales de verdad',
            comment_lower
        ):
            return 'Solicitud - Otros Sabores de Cereal'
        
        # CATEGORÍA 10: NOSTALGIA - Producto que volvió (NUEVA)
        if re.search(
            r'por fin|regresó|volvió|extrañaba|'
            r'no puedo creer.*vuelva|ya salieron|'
            r'al fin|de vuelta',
            comment_lower
        ):
            return 'Nostalgia - Producto que Regresa'
        
        # CATEGORÍA 11: Interés de Compra / Intención (Mejorada)
        if re.search(
            r'\bquiero\b|\bcomprar\b|\besperar\b|\bpapás\b|\bpadres\b|'
            r'voy a|me lo pueden|pedir|conseguir|me gustaría|'
            r'lo prove|lo probé|ya lo probé',
            comment_lower
        ):
            return 'Interés de Compra / Intención'
        
        # CATEGORÍA 12: Disponibilidad en TIENDAS (NUEVA)
        if re.search(
            r'alkosto|ara|éxito|carulla|olímpica|'
            r'dónde.*consigo|dónde hay|en.*tienda|'
            r'vender.*negocio|mi papá.*trajo',
            comment_lower
        ):
            return 'Consultas - Disponibilidad en Tiendas'
        
        # CATEGORÍA 13: Experiencia Positiva - Tamaño/Niños (Mejorada)
        if re.search(
            r'\brico\b|\bbueno\b|\bgusta\b|\bperfecto\b|'
            r'delicioso|me encanta|encanta|deliii|'
            r'tamaño.*perfecto|está perfecto|qué rico|'
            r'son.*rico|demasiado rico',
            comment_lower
        ) and not re.search(r'caro|azúcar|veneno|poquito', comment_lower):
            return 'Experiencia Positiva'
        
        # CATEGORÍA 14: Referencias a LONCHERA/NIÑOS (NUEVA)
        if re.search(
            r'lonchera|lonche|colegio|hijo|hija|niños|niño|'
            r'pequeños|mi bebé|entrar al colegio',
            comment_lower
        ):
            return 'Contexto - Lonchera/Niños'
        
        # CATEGORÍA 15: Opinión sobre la Marca Alpina (Mejorada)
        if re.search(
            r'\balpina\b.*\bmejor\b|\balpina\b.*\bproducción\b|'
            r'calidad alpina|confianza en alpina|productos.*alpina|'
            r'alpina.*mejor',
            comment_lower
        ):
            return 'Opinión Positiva - Marca Alpina'
        
        # CATEGORÍA 16: Quejas sobre SUBIDAS DE PRECIO (NUEVA)
        if re.search(
            r'sube.*precio|subido.*precio|cada mes|cada vez.*caro|'
            r'le han subido',
            comment_lower
        ):
            return 'Críticas - Incremento de Precios'
        
        # CATEGORÍA 17: Spam Religioso (sin cambios)
        if re.search(
            r'\bam[eé]n\b|\bjesús\b|\bpadre\b.*\bcelestial\b|'
            r'bendiciones|padre mio|dios|señor|oración|rosario|'
            r'divina|divino',
            comment_lower
        ):
            return 'Spam Religioso'
        
        # CATEGORÍA 18: Spam de ROBLOX/Juegos (NUEVA - muy frecuente)
        if re.search(
            r'roblox|hartico\.tv|minijuegos|mundo abierto|'
            r'dejaremos de jugar|copia.*pega|1 de marzo',
            comment_lower
        ):
            return 'Spam - Roblox/Juegos'
        
        # CATEGORÍA 19: Menciones de MOCHIS (NUEVA - producto relacionado)
        if re.search(
            r'\bmochi\b|\bmochis\b|mochiiiiiis|nuevos mochis|'
            r'von mochis|dragos|blue lock',
            comment_lower
        ):
            return 'Menciones - Producto Mochis'
        
        # CATEGORÍA 20: Referencias a GABY/Persona (NUEVA - portavoz?)
        if re.search(
            r'\bgaby\b|\bgabi\b|gabiii|gabyy',
            comment_lower
        ):
            return 'Referencias - Gaby (Portavoz/Influencer)'
        
        # CATEGORÍA 21: Solicitudes de Continuación (sin cambios)
        if re.search(
            r'\bparte\s*2\b|\bparte\s*dos\b|\bsiguiente\b.*\bparte\b|'
            r'continúa|continuación|parte 3|parte 6|parte 7',
            comment_lower
        ):
            return 'Solicitudes de Continuación'
        
        # CATEGORÍA 22: Emojis sin texto (NUEVA)
        if re.search(r'^[\s😀-🙏🤍-🫶💯🔥✨]+$', comment_lower) or comment_lower.strip() == '':
            return 'Solo Emojis/Vacío'
        
        # CATEGORÍA 23: Fuera de Tema / No Relevante (Mejorada)
        if re.search(
            r'jajaja|jeje|sicarios|guerrilla|whatsapp|rata campeón|'
            r'veedores|mirla|talento|hermoso niño|linda|guap[oa]|'
            r'hola cómo estás|profesión|salome|fanny silva|'
            r'ojo estos no|verdadera luz|amen amen amen|'
            r'air[oe].*viento|excelente noticia|mini lacto suero|'
            r'\[sticker\]|correcto|total|así es',
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
