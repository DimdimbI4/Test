from django.contrib.auth.models import Group, User

def distribute_user_to_group(user):
    groups = Group.objects.all()

    # Группы с минимальным количеством пользователей
    min_group = min(groups, key=lambda x: x.user_set.count())

    #Проверка, что разница в количестве пользователей между группами не превышает 1
    for group in groups:
        if abs(group.user.count() - min_group.user_set.count()) <= 1:
            min_group = group
            break

    min_group.user_set.add(user)