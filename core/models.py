from django.db import models
unidade
usuario
usuario_unidade
espaco
chave



# Create your models here.
class Unidade(models.Model):
    id_unidade = models.AutoField(_("primary_key"))
    cd_unidade = models.CharField(max_length=20, unique=True, help_text="Ex: 'SENAI-PARA-L'")
    nm_unidade = models.CharField(max_length=150, help_text="Ex: 'SENAI Aparecida de goiânia'")
    cidade = models.CharField(max_length=100, help_text="padrao: 'Aparecida de Goiânia'")


    class Usuario(models.Model):
        id_usuario = models.AutoField(_("primary_key"))
        nm_usuario = models.CharField(max_length=150)
        email = models.EmailField(_("unique"))
        uuid_cracha = models.CharField(max_length=50, unique=True, null=True, blank=True)
        perfil = models.CharField(max_length=50, choices=[('admin', 'Admin'), ('user', 'User')], default='user')
        unidades = models.ManyToManyField(Unidade)
        st_ativo = models.BooleanField(default=True)

        class espaco(models.Model):
            id_espaco = models.AutoField(_("primary_key"))
            cd_espaco = models.CharField(max_length=20, unique=True, help_text="Ex: 'SALA-01'")
            nm_espaco = models.CharField(max_length=150, help_text="Ex: 'Sala de Reunião 01'")
            unidade = models.ForeignKey(Unidade, on_delete=models.CASCADE)

            class chave(models.Model):
                id_chave = models.AutoField(_("primary_key"))
                cd_chave = models.CharField(max_length=20, unique=True, help_text="Ex: 'CHAVE-01'")
                nm_chave = models.CharField(max_length=150, help_text="Ex: 'Chave da Sala de Reunião 01'")
                espaco = models.ForeignKey(espaco, on_delete=models.CASCADE)
                st_disponivel = models.BooleanField(default=True)
                uuid_chave = models.CharField(max_length=50, unique=True, null=True, blank=True)