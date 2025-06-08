"""Módulo para manejar notificaciones de usuarios"""

async def create_notification(user_id, title, message, notification_type="info"):
    """Crea notificación"""
    pass

async def get_user_notifications(user_id, unread_only=False):
    """Obtiene notificaciones del usuario"""
    pass

async def mark_notification_as_read(notification_id):
    """Marca notificación como leída"""
    pass

async def send_email_notification(recipient, subject, message):
    """Envía notificación por email"""
    pass

async def schedule_notification(user_id, title, message, scheduled_time):
    """Programa notificación"""
    pass