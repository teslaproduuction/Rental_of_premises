from django.contrib import admin

# Register your models here.
from .models import *
from django.contrib.auth.admin import UserAdmin


# admin.site.register(Adres)
# admin.site.register(CelArendy)
# admin.site.register(Dogovor)
# admin.site.register(Dolzhnost)
# admin.site.register(DopolnitelnojUslugi)
# admin.site.register(Firma)
# admin.site.register(PasportnyeDannye)
# admin.site.register(Polzovatel)
# admin.site.register(Pomeschenie)
# admin.site.register(Roll)
# admin.site.register(TipPlatyZaPomeshchenie)
# admin.site.register(VidOtdelki)
# admin.site.register(Zdanie)

class AdresAdmin(admin.ModelAdmin):
    list_display = ('Strana', 'Gorod', 'Ulica', 'Dom', 'Kvartira', 'Indeks')
    list_filter = ('Strana', 'Gorod', 'Ulica', 'Dom', 'Kvartira', 'Indeks')
    search_fields = ('Strana', 'Gorod', 'Ulica', 'Dom', 'Kvartira', 'Indeks')


admin.site.register(Adres, AdresAdmin)


class CelArendyAdmin(admin.ModelAdmin):
    list_display = ('NaimenovanieCeli',)
    list_filter = ('NaimenovanieCeli',)
    search_fields = ('NaimenovanieCeli',)


admin.site.register(CelArendy, CelArendyAdmin)


class DogovorAdmin(admin.ModelAdmin):
    readonly_fields = ["KonechnayaCena", 'SrokArendy']
    list_display = ('DataNachala', 'DataOkonchaniia', 'Shtraf', 'SrokArendy', 'KonechnayaCena',)
    list_filter = ('DataNachala', 'DataOkonchaniia', 'Shtraf', 'SrokArendy', 'KonechnayaCena',)
    search_fields = ('DataNachala', 'DataOkonchaniia', 'Shtraf', 'SrokArendy', 'KonechnayaCena', 'SUMM',)


admin.site.register(Dogovor, DogovorAdmin)


class DolzhnostAdmin(admin.ModelAdmin):
    list_display = ('NaimenovanieDolzhnosti', 'Oklad',)
    list_filter = ('NaimenovanieDolzhnosti', 'Oklad',)
    search_fields = ('NaimenovanieDolzhnosti', 'Oklad',)


admin.site.register(Dolzhnost, DolzhnostAdmin)


class DopolnitelnojUslugiAdmin(admin.ModelAdmin):
    list_display = ('NaimenovanieUslugi', 'CenaUslugi',)
    list_filter = ('NaimenovanieUslugi', 'CenaUslugi',)
    search_fields = ('NaimenovanieUslugi', 'CenaUslugi',)


admin.site.register(DopolnitelnojUslugi, DopolnitelnojUslugiAdmin)


class FirmaAdmin(admin.ModelAdmin):
    list_display = ('NaimenovanieFirmy', 'Logotip', 'INN', 'KPP', 'RaschetnySchet', 'Bank',)
    list_filter = ('NaimenovanieFirmy', 'Logotip', 'INN', 'KPP', 'RaschetnySchet', 'Bank',)
    search_fields = ('NaimenovanieFirmy', 'Logotip', 'INN', 'KPP', 'RaschetnySchet', 'Bank',)


admin.site.register(Firma, FirmaAdmin)


class PasportnyeDannyeAdmin(admin.ModelAdmin):
    list_display = ('Seriya', 'Nomer', 'KemVydan', 'DataVydachi', 'KodPodrazdeleniya',)
    list_filter = ('Seriya', 'Nomer', 'KemVydan', 'DataVydachi', 'KodPodrazdeleniya',)
    search_fields = ('Seriya', 'Nomer', 'KemVydan', 'DataVydachi', 'KodPodrazdeleniya',)


admin.site.register(PasportnyeDannye, PasportnyeDannyeAdmin)


class PomeschenieAdmin(admin.ModelAdmin):
    list_display = ('NomerKomnaty', 'PoleznaiaPloshad', 'NomerEtazha', 'Telefon', 'RazmerArendy', 'CenaArendy',)
    list_filter = ('NomerKomnaty', 'PoleznaiaPloshad', 'NomerEtazha', 'Telefon', 'RazmerArendy', 'CenaArendy',)
    search_fields = ('NomerKomnaty', 'PoleznaiaPloshad', 'NomerEtazha', 'Telefon', 'RazmerArendy', 'CenaArendy',)


admin.site.register(Pomeschenie, PomeschenieAdmin)


class TipPlatyZaPomeshchenieAdmin(admin.ModelAdmin):
    list_display = ('NaimenovanieOplaty',)
    list_filter = ('NaimenovanieOplaty',)
    search_fields = ('NaimenovanieOplaty',)


admin.site.register(TipPlatyZaPomeshchenie, TipPlatyZaPomeshchenieAdmin)


class VidOtdelkiAdmin(admin.ModelAdmin):
    list_display = ('NaimenovanieOtdelki',)
    list_filter = ('NaimenovanieOtdelki',)
    search_fields = ('NaimenovanieOtdelki',)


admin.site.register(VidOtdelki, VidOtdelkiAdmin)


class ZdanieAdmin(admin.ModelAdmin):
    list_display = (
        'NaimenovanieZdaniya', 'ChisloEtazhey', 'KolvoPomescheniy', 'TelefonKomendanta', 'id_adres', 'id_firma')
    list_filter = (
        'NaimenovanieZdaniya', 'ChisloEtazhey', 'KolvoPomescheniy', 'TelefonKomendanta', 'id_adres', 'id_firma')
    search_fields = (
        'NaimenovanieZdaniya', 'ChisloEtazhey', 'KolvoPomescheniy', 'TelefonKomendanta', 'id_adres', 'id_firma')


admin.site.register(Zdanie, ZdanieAdmin)

fields = list(UserAdmin.fieldsets)
fields[0] = (None, {'fields': ('username', 'password', 'Fotografiya', 'TelefonPolzovatelya', 'id_adres', 'id_pasportnyedannye', 'id_dolzhnost')})
UserAdmin.fieldsets = tuple(fields)

admin.site.register(User, UserAdmin)
