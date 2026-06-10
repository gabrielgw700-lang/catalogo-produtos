from django.db import models


class Categoria(models.Model):
    nome = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.nome


class Produto(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    imagem = models.ImageField(upload_to='produtos/', blank=True, null=True)
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.CASCADE,
        related_name='produtos',
        null=True, blank=True
    )
    metadados = models.JSONField(default=dict, blank=True)
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome


class Pedido(models.Model):
    STATUS = [
        ('pendente', 'Pendente'),
        ('confirmado', 'Confirmado'),
        ('enviado', 'Enviado'),
        ('cancelado', 'Cancelado'),
    ]
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20, choices=STATUS, default='pendente')

    class Meta:
        ordering = ['-criado_em']

    def __str__(self):
        return f'Pedido #{self.pk} - {self.status}'

    @property
    def total(self):
        return sum(item.subtotal for item in self.itens.all())


class ItemPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name='itens')
    produto = models.ForeignKey(Produto, on_delete=models.PROTECT)
    quantidade = models.PositiveIntegerField(default=1)
    preco_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        unique_together = ['pedido', 'produto']

    def __str__(self):
        return f'{self.quantidade}x {self.produto.nome}'

    @property
    def subtotal(self):
        return self.quantidade * self.preco_unitario