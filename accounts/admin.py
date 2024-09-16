from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from .models import User
 
 
class CustomUserAdmin(UserAdmin):
    # 管理画面でユーザー編集ページで編集できるフィールドを設定できる。
    fieldsets = (
        (None, {
            'fields': (
                'username',
                'email',
                'password',
                'text',
                
            )
        }),
        ('Permissions', {
            'fields': (
                'is_active',
            )
        }),
        ('Admin', {
            'fields': (
                'is_admin',
            )
        })
    )
    list_display = ('username', 'email', 'is_active', ) # 管理画面で設定したアカウントデータを編集できる
    list_filter = () # 管理画面のリストviewで使用するフィルタオプションを指定できる
    ordering = () # リストビューで表示されるユーザーの順序を指定する
    filter_horizontal = () # 多対多フィールドに対して管理画面の編集フォームに
 
    # --- adminでuser作成用に追加 ---
    # 管理画面で新しいユーザーを作成するときに使用する。
    add_fieldsets = (
        (None, {
            'fields': ('username', 'email', 'password',),
        }),
    )
    # --- adminでuser作成用に追加 ---
 
 
admin.site.unregister(Group)
admin.site.register(User, CustomUserAdmin)