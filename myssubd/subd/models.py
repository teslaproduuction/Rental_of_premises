from django.core.validators import RegexValidator, MinValueValidator
from django.db.models import CharField
from django.urls import reverse
from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import datetime


class Adres(models.Model):
    Strana = models.CharField(max_length=50, verbose_name='Страна', help_text='Введите страну')
    Gorod = models.CharField(max_length=50, verbose_name='Город', help_text='Введите город')
    Ulica = models.CharField(max_length=50, verbose_name='Улица', help_text='Введите улицу')
    Dom = models.CharField(max_length=50, verbose_name='Дом', help_text='Введите дом')
    Kvartira = models.CharField(max_length=50, verbose_name='Квартира', null=True, blank=True,
                                help_text='Введите квартиру')
    Indeks = models.CharField(max_length=50, verbose_name='Индекс', help_text='Введите индекс')

    class Meta:
        verbose_name = 'Адрес'
        verbose_name_plural = 'Адреса'

    def __str__(self):
        return u'{} , {} , {} , {}'.format(self.Strana, self.Gorod, self.Ulica, self.Dom)


class VidOtdelki(models.Model):
    NaimenovanieOtdelki = models.CharField(max_length=50, verbose_name='Наименование отделки',
                                           help_text='Введите наименование отделки')

    class Meta:
        verbose_name = 'Вид отделки'
        verbose_name_plural = 'Виды отделки'

    def __str__(self):
        return self.NaimenovanieOtdelki


class Dolzhnost(models.Model):
    NaimenovanieDolzhnosti = models.CharField(max_length=150, verbose_name='Наименование должности',
                                              help_text='Введите наименование должности')
    Oklad = models.IntegerField(verbose_name='Оклад', help_text='Введите оклад')

    class Meta:
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'

    def __str__(self):
        return self.NaimenovanieDolzhnosti


class CelArendy(models.Model):
    NaimenovanieCeli = models.CharField(max_length=50, verbose_name='Наименование цели',
                                        help_text='Введите наименование цели')

    class Meta:
        verbose_name = 'Цель аренды'
        verbose_name_plural = 'Цели аренды'

    def __str__(self):
        return self.NaimenovanieCeli


class DopolnitelnojUslugi(models.Model):
    NaimenovanieUslugi = models.CharField(max_length=50, verbose_name='Наименование услуги',
                                          help_text='Введите наименование услуги')
    CenaUslugi = models.IntegerField(verbose_name='Цена услуги', help_text='Введите цену услуги')

    class Meta:
        verbose_name = 'Дополнительная услуга'
        verbose_name_plural = 'Дополнительные услуги'

    def __str__(self):
        return self.NaimenovanieUslugi


class TipPlatyZaPomeshchenie(models.Model):
    NaimenovanieOplaty = models.CharField(max_length=50, verbose_name='Наименование оплаты',
                                          help_text='Введите наименование оплаты')

    class Meta:
        verbose_name = 'Тип оплаты'
        verbose_name_plural = 'Типы оплаты'

    def __str__(self):
        return self.NaimenovanieOplaty


class PasportnyeDannye(models.Model):
    Seriya = models.CharField(max_length=5, verbose_name='Серия', help_text='Введите серию', validators=[RegexValidator(r'^[0-9]{2}[ ]{1}[0-9]{2}$', message='Серия должна быть в формате XX XX')])
    Nomer = models.CharField(max_length=6, verbose_name='Номер', help_text='Введите номер')
    KemVydan = models.CharField(max_length=50, verbose_name='Кем выдан', help_text='Введите кем выдан')
    DataVydachi = models.DateField(verbose_name='Дата выдачи', help_text='Введите дату выдачи')
    KodPodrazdeleniya = models.CharField(max_length=7, verbose_name='Код подразделения',
                                         help_text='Введите код подразделения', validators=[RegexValidator(r'^[0-9]{3}[-]{1}[0-9]{3}$', message='Код подразделения должен быть в формате XXX-XXX')])

    class Meta:
        verbose_name = 'Паспортные данные'
        verbose_name_plural = 'Паспортные данные'

    def __str__(self):
        return u'%s %s' % (self.Seriya, self.Nomer)


class User(AbstractUser):
    Fotografiya = models.ImageField(upload_to='img/', null=True, blank=True, default='/img/Blank.png', help_text='Ссылка на фотографию',
                                    verbose_name='Фотография')
    TelefonPolzovatelya = models.CharField(max_length=16, verbose_name='Телефон пользователя',
                                           help_text='Введите телефон пользователя', blank=True, null=True,validators=[RegexValidator(r'^[+]{1}[0-9]{1}[(]{1}[0-9]{3}[)]{1}[0-9]{3}[-]{1}[0-9]{2}[-]{1}[0-9]{2}$', message='Номер телефона должен быть в формате +X(XXX)XXX-XX-XX')])
    id_pasportnyedannye = models.ForeignKey(PasportnyeDannye, on_delete=models.CASCADE, null=True,
                                            help_text='Выберете паспортные данные пользователя',
                                            verbose_name='Паспортные данные пользователя', blank=True, )
    id_dolzhnost = models.ForeignKey(Dolzhnost, on_delete=models.CASCADE, null=True,
                                     help_text='Выберете должность пользователя', verbose_name='Должность пользователя')
    id_adres = models.ForeignKey(Adres, on_delete=models.CASCADE, null=True, help_text='Выберете адрес пользователя',
                                 verbose_name='Адрес пользователя')

    def __str__(self):
        return self.username


class Firma(models.Model):
    NaimenovanieFirmy = models.CharField(max_length=150, null=True, blank=True, help_text='Введите название',
                                         verbose_name='Название')
    Logotip = models.ImageField(upload_to='img/', null=True, blank=True, help_text='Ссылка на фотографию',
                                verbose_name='Фотография')
    INN = models.CharField(max_length=12, help_text='Введите ИНН', null=True, blank=True, verbose_name='ИНН')
    RaschetnySchet = models.CharField(max_length=20, help_text='Введите расчетный счет', null=True, blank=True,
                                      verbose_name='Расчетный счет')
    KPP = models.CharField(max_length=9, help_text='Введите КПП', null=True, blank=True, verbose_name='КПП', validators=[RegexValidator(r'^[0-9]{9}$', message='КПП должен быть в формате ХХХХХХХХХ')])
    Bank = models.CharField(max_length=50, help_text='Введите банк', verbose_name='Банк')
    id_adres = models.ForeignKey(Adres, on_delete=models.CASCADE, null=True, help_text='Выберете адрес',
                                 verbose_name='Адрес')
    id_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True,
                                help_text='Выберете пользователя', verbose_name='Пользователь')

    class Meta:
        verbose_name = 'Фирма'
        verbose_name_plural = 'Фирмы'

    def __str__(self):
        return u'%s' % (self.NaimenovanieFirmy)


class Zdanie(models.Model):
    NaimenovanieZdaniya = models.CharField(max_length=50, help_text='Введите название', verbose_name='Название')
    ChisloEtazhey = models.IntegerField(help_text='Введите количество этажей', verbose_name='Количество этажей', validators=[MinValueValidator(0)])
    KolvoPomescheniy = models.IntegerField(help_text='Введите количество помещений', validators=[MinValueValidator(0)],
                                           verbose_name='Количество помещений')
    TelefonKomendanta = models.CharField(max_length=16, verbose_name='Телефон здания',
                                         help_text='Введите телефон здания', validators=[RegexValidator(r'^[+]{1}[0-9]{1}[(]{1}[0-9]{3}[)]{1}[0-9]{3}[-]{1}[0-9]{2}[-]{1}[0-9]{2}$', message='Номер телефона должен быть в формате +X(XXX)XXX-XX-XX')])
    id_adres = models.ForeignKey(Adres, on_delete=models.CASCADE, null=True, help_text='Выберете адрес',
                                 verbose_name='Адрес')
    id_firma = models.ForeignKey(Firma, on_delete=models.CASCADE, null=True, help_text='Выберете фирму',
                                 verbose_name='Фирма')

    class Meta:
        verbose_name = 'Здание'
        verbose_name_plural = 'Здания'

    def __str__(self):
        return self.NaimenovanieZdaniya


class Pomeschenie(models.Model):
    NomerKomnaty = models.IntegerField(help_text='Введите номер комнаты', verbose_name='Номер комнаты')
    Opisanie = models.TextField(help_text='Введите описание', verbose_name='Описание', null=True)
    PoleznaiaPloshad = models.IntegerField(help_text='Введите площадь', verbose_name='Площадь')
    NomerEtazha = models.IntegerField(help_text='Введите номер этажа', verbose_name='Номер этажа')
    Telefon = models.CharField(max_length=16, verbose_name='Телефон комнаты', help_text='Введите телефон комнаты', validators=[RegexValidator(r'^[+]{1}[0-9]{1}[(]{1}[0-9]{3}[)]{1}[0-9]{3}[-]{1}[0-9]{2}[-]{1}[0-9]{2}$', message='Номер телефона должен быть в формате +X(XXX)XXX-XX-XX')])
    RazmerArendy = models.IntegerField(help_text='Введите стоимость помещения', verbose_name='Стоимость помещения')
    Photo = models.ImageField(upload_to='img/', null=True, blank=True, help_text='Ссылка на фотографию', default='/img/Pomdef.jpg', verbose_name='Фотография')
    CenaArendy = models.IntegerField(help_text='Введите цену аренды', verbose_name='Цена аренды')
    id_zdanie = models.ForeignKey(Zdanie, on_delete=models.CASCADE, null=True, help_text='Выберете здание',
                                  verbose_name='Здание')
    id_vidotdelki = models.ForeignKey(VidOtdelki, on_delete=models.CASCADE, null=True, help_text='Выберете вид отделки',
                                      verbose_name='Вид отделки')
    id_celi = models.ForeignKey(CelArendy, on_delete=models.CASCADE, null=True, help_text='Выберете цель',
                                verbose_name='Цель')

    class Meta:
        verbose_name = 'Помещение'
        verbose_name_plural = 'Помещения'

    def __str__(self):
        return u'%sm², %s, %s, %s₽' % (self.PoleznaiaPloshad, self.NomerEtazha, self.Telefon, self.CenaArendy)


class Dogovor(models.Model):
    DataNachala = models.DateField(help_text='Введите дату заключения', verbose_name='Дата заключения')
    DataOkonchaniia = models.DateField(help_text='Введите дату окончания', verbose_name='Дата окончания')
    Shtraf = models.IntegerField(help_text='Введите штраф', verbose_name='Штраф', validators=[MinValueValidator(0)])
    SrokArendy = models.IntegerField(help_text='Введите срок аренды', verbose_name='Срок аренды', null=True, blank=True)
    KonechnayaCena = models.IntegerField(help_text='Введите конечную цену', null=True, blank=True,
                                         verbose_name='Конечная цена')
    id_dopolnitelnojuslugi = models.ForeignKey(DopolnitelnojUslugi, on_delete=models.CASCADE, null=True,
                                               help_text='Выберете дополнительные услуги',
                                               verbose_name='Дополнительные услуги')
    id_TipPlatyZaPomeshchenie = models.ForeignKey(TipPlatyZaPomeshchenie, on_delete=models.CASCADE, null=True,
                                                  help_text='Выберете тип платы за помещение',
                                                  verbose_name='Тип платы за помещение')
    id_pomeschenie = models.ForeignKey(Pomeschenie, on_delete=models.CASCADE, null=True, help_text='Выберете помещение',
                                       verbose_name='Помещение')
    id_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True,
                                help_text='Выберете пользователя', verbose_name='Пользователь')

    class Meta:
        verbose_name = 'Договор'
        verbose_name_plural = 'Договора'

    def save(self, *args, **kwargs):
        if self.id_TipPlatyZaPomeshchenie == TipPlatyZaPomeshchenie.objects.get(NaimenovanieOplaty='Ежемесячно'):
            self.SrokArendy = int((self.DataOkonchaniia - self.DataNachala).days) / 30
        elif self.id_TipPlatyZaPomeshchenie == TipPlatyZaPomeshchenie.objects.get(NaimenovanieOplaty='Погодовая'):
            self.SrokArendy = int((self.DataOkonchaniia - self.DataNachala).days) / 365
        elif self.id_TipPlatyZaPomeshchenie == TipPlatyZaPomeshchenie.objects.get(NaimenovanieOplaty='Посуточная'):
            self.SrokArendy = int((self.DataOkonchaniia - self.DataNachala).days)
        elif self.id_TipPlatyZaPomeshchenie == TipPlatyZaPomeshchenie.objects.get(NaimenovanieOplaty='Поквартально'):
            self.SrokArendy = int((self.DataOkonchaniia - self.DataNachala).days) / 30 * 3
        else:
            self.SrokArendy = int((self.DataOkonchaniia - self.DataNachala).days)
        self.KonechnayaCena = self.id_pomeschenie.CenaArendy * self.SrokArendy + self.Shtraf + self.id_dopolnitelnojuslugi.CenaUslugi
        super(Dogovor, self).save(*args, **kwargs)

    def __str__(self):
        return u'%s, %s, %s, %s₽' % (self.DataNachala, self.DataOkonchaniia, self.SrokArendy, self.KonechnayaCena)
