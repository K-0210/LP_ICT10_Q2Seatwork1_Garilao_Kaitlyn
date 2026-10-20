from pyscript import document

def candidate_checker(e):
    club_members = ['Mia Padillo', 'Jade Saquido', 'Athena Silva', 'Ninah Lim', 'Kaitlyn Garilao', 'Sage Aguinaldo', 'Olivia Lopez', 'Maverice Catisag', 'Kate Dela Calzada', 'Constance Magday']
    small_letters = [name.lower() for name in club_members]
    f_name = document.getElementById('first_name').value
    l_name = document.getElementById('last_name').value
    candidate = f_name + ' ' + l_name
    member_checker = candidate in club_members or candidate.lower() in small_letters

    messages = (f'Sorry {candidate}, your name is not on the list!',
                f'Congratulations {candidate}! You are now part of the Cosmic Writers Guild!')

    document.getElementById('result').innerHTML =messages[member_checker]