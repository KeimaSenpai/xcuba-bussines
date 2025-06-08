"""Módulo para manejar clientes """

async def create_customer(company_id, name, email, phone, address, customer_type="individual"):
    """Crea un nuevo cliente"""
    pass

async def get_customer_by_id(customer_id):
    """Obtiene cliente por ID"""
    pass

async def get_customers_by_company(company_id):
    """Obtiene clientes de una empresa"""
    pass

async def update_customer(customer_id, **kwargs):
    """Actualiza datos del cliente"""
    pass

async def delete_customer(customer_id):
    """Elimina cliente"""
    pass

async def search_customers(company_id, search_term):
    """Busca clientes por nombre/email"""
    pass

async def get_customer_purchase_history(customer_id):
    """Obtiene historial de compras del cliente"""
    pass