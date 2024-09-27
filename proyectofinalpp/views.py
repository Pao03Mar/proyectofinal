from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Venta, Caja, Empleado, Compra, DetalleVenta, DetalleCompra, Producto, Proveedor, ProdProv
from .forms import VentaForm, CajaForm, EmpleadoForm, CompraForm, DetalleVentaForm, DetalleCompraForm, ProductoForm, ProveedorForm, ProdProvForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import logout
import json
def logout(request):
    logout(request)
    return redirect('login')
# Página de inicio
@login_required
def inicio(request):
    ventas = Venta.objects.all()
    cajas = Caja.objects.all()
    compras = Compra.objects.all()
    
    context = {
        'ventas': ventas,
        'cajas': cajas,
        'compras': compras,
    }
    
    return render(request, 'inicio.html', context)

# Vistas para Ventas
class VentaListView(ListView):
    model = Venta
    template_name = 'ventas/lista_ventas.html'
    context_object_name = 'ventas'

class VentaCreateView(CreateView):
    model = Venta
    form_class = VentaForm
    template_name = 'ventas/crear_venta.html'
    success_url = reverse_lazy('ventas_list')  
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Pasar productos y sus precios al contexto
        productos = Producto.objects.all()
        context['productos_precios_json'] = json.dumps({producto.idProducto: producto.Precio for producto in productos})
        return context
    def form_valid(self, form):
        venta = form.save(commit=False)
        detalles = self.request.POST.getlist('detalleProd_id')  # Obtener todos los IDs de productos
        total = 0
        for detalle_id in detalles:
            try:
                producto = Producto.objects.get(idProducto=detalle_id)
                # Aquí deberías también manejar la cantidad, precio unitario, etc.
                cantidad = self.request.POST.get(f'cantidad_{detalle_id}', 1)  # Por defecto 1 si no se pasa
                total += cantidad*producto.Precio
                detalle = DetalleVenta(
                    venta=venta,
                    producto=producto,
                    cantidad=cantidad,
                    precio_unitario=producto.Precio,
                )
                venta.Productos = producto
                detalle.save()
            except ObjectDoesNotExist:
                print(f"Producto con ID {detalle_id} no existe.")
        # Calcular el total de la venta
        venta.Total_venta = total
        venta.Precio_uni = 0
        venta.Cantidad_vendida = 0
        venta.Garantias = 0
        
        venta.save()
        return super().form_valid(form)

class VentaUpdateView(UpdateView):
    model = Venta
    form_class = VentaForm
    template_name = 'ventas/editar_venta.html'
    success_url = reverse_lazy('ventas_list')

    def form_valid(self, form):
        venta = form.save(commit=False)
        venta.Total_venta = venta.Precio_uni * venta.Cantidad_vendida  # Recalcular el total
        venta.save()
        return super().form_valid(form)

class VentaDeleteView(DeleteView):
    model = Venta
    template_name = 'ventas/eliminar_venta.html'
    success_url = reverse_lazy('ventas_list')

# Vistas para Cajas
class CajaListView(ListView):
    model = Caja
    template_name = 'cajas/lista_cajas.html'
    context_object_name = 'cajas'

class CajaCreateView(CreateView):
    model = Caja
    form_class = CajaForm
    template_name = 'cajas/crear_caja.html'
    success_url = reverse_lazy('cajas_list')

class CajaUpdateView(UpdateView):
    model = Caja
    form_class = CajaForm
    template_name = 'cajas/editar_caja.html'
    success_url = reverse_lazy('cajas_list')

class CajaDeleteView(DeleteView):
    model = Caja
    template_name = 'cajas/eliminar_caja.html'
    success_url = reverse_lazy('cajas_list')

# Vistas para Empleados
class EmpleadoListView(ListView):
    model = Empleado
    template_name = 'empleados/lista_empleados.html'
    context_object_name = 'empleados'

class EmpleadoCreateView(CreateView):
    model = Empleado
    form_class = EmpleadoForm
    template_name = 'empleados/crear_empleado.html'
    success_url = reverse_lazy('empleados_list')

class EmpleadoUpdateView(UpdateView):
    model = Empleado
    form_class = EmpleadoForm
    template_name = 'empleados/editar_empleado.html'
    success_url = reverse_lazy('empleados_list')

class EmpleadoDeleteView(DeleteView):
    model = Empleado
    template_name = 'empleados/eliminar_empleado.html'
    success_url = reverse_lazy('empleados_list')

# Vistas para Compras
class CompraListView(ListView):
    model = Compra
    template_name = 'compras/lista_compras.html'
    context_object_name = 'compras'

class CompraCreateView(CreateView):
    model = Compra
    form_class = CompraForm
    template_name = 'compras/crear_compra.html'
    success_url = reverse_lazy('compras_list')

class CompraUpdateView(UpdateView):
    model = Compra
    form_class = CompraForm
    template_name = 'compras/editar_compra.html'
    success_url = reverse_lazy('compras_list')

class CompraDeleteView(DeleteView):
    model = Compra
    template_name = 'compras/eliminar_compra.html'
    success_url = reverse_lazy('compras_list')

# Vistas para DetalleVenta
class DetalleVentaListView(ListView):
    model = DetalleVenta
    template_name = 'detalle_ventas/lista_detalle_ventas.html'
    context_object_name = 'detalle_ventas'

class DetalleVentaCreateView(CreateView):
    model = DetalleVenta
    form_class = DetalleVentaForm
    template_name = 'detalle_ventas/crear_detalle_venta.html'
    success_url = reverse_lazy('detalle_ventas_list')

class DetalleVentaUpdateView(UpdateView):
    model = DetalleVenta
    form_class = DetalleVentaForm
    template_name = 'detalle_ventas/editar_detalle_venta.html'
    success_url = reverse_lazy('detalle_ventas_list')

class DetalleVentaDeleteView(DeleteView):
    model = DetalleVenta
    template_name = 'detalle_ventas/eliminar_detalle_venta.html'
    success_url = reverse_lazy('detalle_ventas_list')

# Vistas para DetalleCompra
class DetalleCompraListView(ListView):
    model = DetalleCompra
    template_name = 'detalle_compras/lista_detalle_compras.html'
    context_object_name = 'detalle_compras'

class DetalleCompraCreateView(CreateView):
    model = DetalleCompra
    form_class = DetalleCompraForm
    template_name = 'detalle_compras/crear_detalle_compra.html'
    success_url = reverse_lazy('detalle_compras_list')

class DetalleCompraUpdateView(UpdateView):
    model = DetalleCompra
    form_class = DetalleCompraForm
    template_name = 'detalle_compras/editar_detalle_compra.html'
    success_url = reverse_lazy('detalle_compras_list')

class DetalleCompraDeleteView(DeleteView):
    model = DetalleCompra
    template_name = 'detalle_compras/eliminar_detalle_compra.html'
    success_url = reverse_lazy('detalle_compras_list')

# Vistas para Productos
class ProductoListView(ListView):
    model = Producto
    template_name = 'productos/lista_productos.html'
    context_object_name = 'productos'

class ProductoCreateView(CreateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'productos/crear_producto.html'
    success_url = reverse_lazy('productos_list')

class ProductoUpdateView(UpdateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'productos/editar_producto.html'
    success_url = reverse_lazy('productos_list')

class ProductoDeleteView(DeleteView):
    model = Producto
    template_name = 'productos/eliminar_producto.html'
    success_url = reverse_lazy('productos_list')

# Vistas para Proveedores
class ProveedorListView(ListView):
    model = Proveedor
    template_name = 'proveedores/lista_proveedores.html'
    context_object_name = 'proveedores'

class ProveedorCreateView(CreateView):
    model = Proveedor
    form_class = ProveedorForm
    template_name = 'proveedores/crear_proveedor.html'
    success_url = reverse_lazy('proveedores_list')

class ProveedorUpdateView(UpdateView):
    model = Proveedor
    form_class = ProveedorForm
    template_name = 'proveedores/editar_proveedor.html'
    success_url = reverse_lazy('proveedores_list')

class ProveedorDeleteView(DeleteView):
    model = Proveedor
    template_name = 'proveedores/eliminar_proveedor.html'
    success_url = reverse_lazy('proveedores_list')

# Vistas para ProdProv
class ProdProvListView(ListView):
    model = ProdProv
    template_name = 'prod_prov/lista_prod_prov.html'
    context_object_name = 'prod_prov'

class ProdProvCreateView(CreateView):
    model = ProdProv
    form_class = ProdProvForm
    template_name = 'prod_prov/crear_prod_prov.html'
    success_url = reverse_lazy('prod_prov_list')

class ProdProvUpdateView(UpdateView):
    model = ProdProv
    form_class = ProdProvForm
    template_name = 'prod_prov/editar_prod_prov.html'
    success_url = reverse_lazy('prod_prov_list')

class ProdProvDeleteView(DeleteView):
    model = ProdProv
    template_name = 'prod_prov/eliminar_prod_prov.html'
    success_url = reverse_lazy('prod_prov_list')
