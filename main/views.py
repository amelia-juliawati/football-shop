from django.shortcuts import render

def show_main(request):
    context = {
        'nama_toko' : 'Turboa Shop',
        'nama': 'Amelia Juliawati',
        'npm' : '2406414076',
        'kelas' : 'PBP A',
    }

    return render(request, "main.html", context)