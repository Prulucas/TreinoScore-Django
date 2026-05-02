
def is_teacher_or_admin(user):
    return user.is_authenticated and (user.role == 'teacher' or user.is_superuser)
