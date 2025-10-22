from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from simple_history.models import HistoricalRecords

from utils.constants import CustomerType


class Customer(AbstractUser):
    """Modelo de perfil de usuário personalizado.

    O perfil de usuário é baseado no modelo de usuário padrão do Django, mas com
    campos adicionais.

    Atributos herdados:
        - username (str): Nome de usuário.
        - first_name (str): Primeiro nome.
        - last_name (str): Último nome.
        - email (str): Endereço de e-mail.
        - is_staff (bool): Indica se este usuário pode acessar este site de administração.
        - is_active (bool): Indica se este usuário deve ser tratado como ativo.
        - date_joined (datetime): Data e hora em que este usuário foi adicionado.

    Atributos adicionais:
        - CustomerType (str): Tipo de perfil baseado em contants do arquivo
        [contants.CustomerType](../../utils/constants.md#service.src.utils.constants.CustomerType).
        - groups (Group): Grupos de permissões aos quais este usuário pertence.
        - user_permissions (Permission): Permissões específicas para este usuário
    """

    history = HistoricalRecords()

    email = models.EmailField("E-mail", unique=True, blank=False, null=False)

    CustomerType = models.IntegerField(
        "Tipo de Perfil",
        choices=CustomerType.CUSTOMER_TYPE_CHOICES,
        default=CustomerType.EARUSER,
    )

    groups = models.ManyToManyField(
        Group,
        verbose_name="Grupos de Permissões",
        blank=True,
        help_text="Os grupos aos quais este usuário pertence.",
        related_name="usuario_set",
        related_query_name="usuario",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name="Permissões de Usuários",
        blank=True,
        help_text="Permissões específicas para este usuário.",
        related_name="usuario_permissions",
        related_query_name="usuario",
    )

    def __str__(self):
        return f"{self.get_full_name()} ({self.username})"

    class Meta:
        verbose_name = "Customer"
        verbose_name_plural = "Customers"
