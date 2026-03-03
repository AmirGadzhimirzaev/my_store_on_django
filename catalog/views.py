from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView

from catalog.forms import ProductForm, ProductModeratorForm
from catalog.models import Product, Category
from catalog.services import get_prod_from_cache, get_category_prods_list


class HomeTemplateView(LoginRequiredMixin, TemplateView):
    template_name = '../templates/catalog/home.html'


class ContactsTemplateView(LoginRequiredMixin, TemplateView):
    template_name = '../templates/catalog/contacts.html'


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product_list')

    def form_valid(self, form):
        product = form.save()
        user = self.request.user
        product.owner = user
        product.save()

        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product_list')

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data["formset"]
        if form.is_valid() and formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return super().form_valid(form)
        else:
            return self.render_to_response(self.get_context_data(form=form, formset=formset))

    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner:
            return ProductForm
        if user.has_perm('catalog.can_unpublish_product') and user.has_perm('catalog.delete_product'):
            return ProductModeratorForm
        raise PermissionDenied


class ProductListView(ListView):
    model = Product

    def get_queryset(self):
        return get_prod_from_cache()


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.request.user == self.object.owner or self.request.user.is_authenticated:
            self.object.views_counter += 1
            self.object.save()
            return self.object
        raise PermissionDenied


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:product_list')

    def get_object(self, queryset=None):
        user = self.request.user
        self.object = super().get_object(queryset)
        if self.request.user == self.object.owner or user.has_perm('catalog.can_unpublish_product'):
            return self.object
        raise PermissionDenied


class CategoryListView(LoginRequiredMixin, ListView):
    model = Category
