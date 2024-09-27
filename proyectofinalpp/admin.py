from django.contrib import admin
from .models import Venta, Caja, Empleado, Compra, DetalleVenta, DetalleCompra, Producto, Proveedor, ProdProv

# Admin para el modelo Venta
class VentaAdmin(admin.ModelAdmin):
    list_display = ['idVentas', 'Fecha_hora_venta', 'Garantias', 'Precio_uni', 'Metodo_pago', 'Total_venta', 'VENT_AtGral']  # Elimina 'Productos'
    search_fields = ['Garantias']  # Elimina 'Productos'
    list_filter = ['Metodo_pago']

# Admin para el modelo Caja
class CajaAdmin(admin.ModelAdmin):
    list_display = ['idCajas', 'Saldo_inicial', 'Fecha_Apertura', 'Fecha_Cierre', 'id_Empleados']
    search_fields = ['id_Empleados']

# Admin para otros modelos
admin.site.register(Venta, VentaAdmin)
admin.site.register(Caja, CajaAdmin)
admin.site.register(Empleado)
admin.site.register(Compra)
admin.site.register(DetalleVenta)
admin.site.register(DetalleCompra)
admin.site.register(Producto)
admin.site.register(Proveedor)
admin.site.register(ProdProv)
