from django import forms
from .models import Venta, Caja, Empleado, Compra, DetalleVenta, DetalleCompra, Producto, Proveedor, ProdProv

# Formulario para Ventas
# forms.py
from django import forms
from .models import Venta

class VentaForm(forms.ModelForm):
    class Meta:
        model = Venta
        fields = ['Fecha_hora_venta', 'Garantias', 'Productos', 'Precio_uni', 'Metodo_pago', 'Cantidad_vendida', 'Total_venta', 'VENT_AtGral']
        labels = {
            'Fecha_hora_venta': 'Fecha y Hora de la Venta',
            'Garantias': 'Garantías',
            'Productos': 'Producto',
            'Precio_uni': 'Precio Unitario',
            'Metodo_pago': 'Método de Pago',
            'Cantidad_vendida': 'Cantidad Vendida',
            'Total_venta': 'Total de la Venta',
            'VENT_AtGral': 'Venta General',
        }
        widgets = {
            'Fecha_hora_venta': forms.DateTimeInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'Garantias': forms.TextInput(attrs={'class': 'form-control'}),
            'Productos': forms.Select(attrs={'class': 'form-control'}),
            'Precio_uni': forms.NumberInput(attrs={'class': 'form-control'}),
            'Metodo_pago': forms.Select(attrs={'class': 'form-control'}),
            'Cantidad_vendida': forms.NumberInput(attrs={'class': 'form-control'}),
            'Total_venta': forms.NumberInput(attrs={'class': 'form-control'}),
            'VENT_AtGral': forms.TextInput(attrs={'class': 'form-control'}),
        }

    # Usamos __init__ para modificar los campos
    def __init__(self, *args, **kwargs):
        super(VentaForm, self).__init__(*args, **kwargs)
        # Hacemos todos los campos no obligatorios
        self.fields['Fecha_hora_venta'].required = False
        self.fields['Garantias'].required = False
        self.fields['Productos'].required = False
        self.fields['Precio_uni'].required = False
        self.fields['Metodo_pago'].required = False
        self.fields['Cantidad_vendida'].required = False
        self.fields['Total_venta'].required = False
        self.fields['VENT_AtGral'].required = False



# Formulario para Cajas
class CajaForm(forms.ModelForm):
    class Meta:
        model = Caja
        fields = ['Saldo_inicial', 'Fecha_Apertura', 'Fecha_Cierre', 'id_Empleados']
        labels = {
            'Saldo_inicial': 'Saldo Inicial',
            'Fecha_Apertura': 'Fecha de Apertura',
            'Fecha_Cierre': 'Fecha de Cierre',
            'id_Empleados': 'ID del Empleado',
        }

# Formulario para Empleados
class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = ['Telefono', 'No_Documento', 'Direccion']
        labels = {
            'Telefono': 'Teléfono',
            'No_Documento': 'Número de Documento',
            'Direccion': 'Dirección',
        }

# Formulario para Compras
class CompraForm(forms.ModelForm):
    class Meta:
        model = Compra
        fields = ['Fecha_hora_compra', 'Nro_Compra', 'Metodo_pago', 'Producto', 'Precio', 'Cantidad', 'Total_compra', 'id_proveedor']
        labels = {
            'Fecha_hora_compra': 'Fecha y Hora de la Compra',
            'Nro_Compra': 'Número de Compra',
            'Metodo_pago': 'Método de Pago',
            'Producto': 'Producto',
            'Precio': 'Precio',
            'Cantidad': 'Cantidad',
            'Total_compra': 'Total de la Compra',
            'id_proveedor': 'ID del Proveedor',
        }

# Formulario para Detalle de Ventas
class DetalleVentaForm(forms.ModelForm):
    class Meta:
        model = DetalleVenta
        fields = ['idVentas', 'idProducto', 'Cant_vendida', 'Prec_uni']
        labels = {
            'idVentas': 'ID de la Venta',
            'idProducto': 'ID del Producto',
            'Cant_vendida': 'Cantidad Vendida',
            'Prec_uni': 'Precio Unitario',
        }

# Formulario para Detalle de Compras
class DetalleCompraForm(forms.ModelForm):
    class Meta:
        model = DetalleCompra
        fields = ['idCompra', 'idProducto', 'Cant_Comprada', 'Prec_uni']
        labels = {
            'idCompra': 'ID de la Compra',
            'idProducto': 'ID del Producto',
            'Cant_Comprada': 'Cantidad Comprada',
            'Prec_uni': 'Precio Unitario',
        }

# Formulario para Productos
class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['Nombre', 'Descripcion', 'Precio', 'Stock', 'Marca']
        labels = {
            'Nombre': 'Nombre del Producto',
            'Descripcion': 'Descripción',
            'Precio': 'Precio',
            'Stock': 'Stock',
            'Marca': 'Marca',
        }

# Formulario para Proveedores
class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = ['CUIT', 'Telefono', 'Correo', 'Domicilio', 'Nombre']
        labels = {
            'CUIT': 'CUIT',
            'Telefono': 'Teléfono',
            'Correo': 'Correo Electrónico',
            'Domicilio': 'Domicilio',
            'Nombre': 'Nombre del Proveedor',
        }

# Formulario para Prod_Prov
class ProdProvForm(forms.ModelForm):
    class Meta:
        model = ProdProv
        fields = ['idProducto', 'id_proveedor']
        labels = {
            'idProducto': 'ID del Producto',
            'id_proveedor': 'ID del Proveedor',
        }
