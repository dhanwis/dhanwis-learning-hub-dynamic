from django.shortcuts import render, redirect
from admin_app.models import *
from django.contrib.auth.decorators import login_required

# add your views here.


@login_required(login_url='/auth/admin/login/')
def dashboard(request):
    current_page = 'dashboard'
    context = {
        'current_page': current_page,
    }
    return render(request, 'admin_app/dashboard.html', context)

@login_required(login_url='/auth/admin/login/')
def course_add(request):
    if request.method == 'POST':
        image = request.FILES.get('image')
        heading = request.POST.get('heading')
        description = request.POST.get('description')
        duraction = request.POST.get('duraction')
        
        course = Course(
            image=image,  
            heading=heading,
            description=description,
            duraction=duraction,
        )
        course.save()
        return redirect('course-list')
    else:
        return render(request, 'admin_app/course-add.html')

@login_required(login_url='/auth/admin/login/')
def course_list(request):
    courses = Course.objects.all()
    context = {
        'courses': courses
    }
    return render(request, 'admin_app/course-list.html', context)

@login_required(login_url='/auth/admin/login/')
def course_edit(request, course_id):
    try:
        course = Course.objects.get(id=course_id)
    except Course.DoesNotExist:
        return render(request, 'admin_app/page-not-found.html') 

    if request.method == 'POST':
        new_image = request.FILES.get('image')
        if new_image:
            course.image = new_image
        else:
            new_image = course.image
        course.heading = request.POST.get('heading')
        course.description = request.POST.get('description')
        course.duraction = request.POST.get('duraction')
        course.save()
        return redirect('course-list')

    context = {
        'course': course
    }

    return render(request, 'admin_app/course-edit.html', context)

@login_required(login_url='/auth/admin/login/')
def course_delete(request, course_id):
    try:
        course = Course.objects.get(id=course_id)
    except Course.DoesNotExist:
        return render(request, 'admin_app/page-not-found.html')  

    course.delete()
    return redirect('course-list')



@login_required(login_url='/auth/admin/login/')
def company_list(request):
    companies = Company.objects.all()
    return render(request, 'admin_app/company-list.html', {'companies': companies})

@login_required(login_url='/auth/admin/login/')
def company_detail(request, company_id):
    company = Company.objects.get(id=company_id)
    return render(request, 'admin_app/company-detail.html', {'company': company})

@login_required(login_url='/auth/admin/login/')
def company_add(request):
    if request.method == 'POST':
        image = request.FILES.get('image')
        url = request.POST.get('url')

        if image and url:
            new_company = Company(image=image, url=url)
            new_company.save()
            return redirect('company-list')
        
    else:
        return render(request, 'admin_app/company-add.html')

@login_required(login_url='/auth/admin/login/')
def company_edit(request, company_id):
    company = Company.objects.get(id=company_id)

    if request.method == 'POST':
        new_image = request.FILES.get('image')
        if new_image:
            company.image = new_image
        else:
            new_image = company.image
        company.url = request.POST.get('url')
        company.save()
        return redirect('company-list')
    else:
        return render(request, 'admin_app/company-edit.html', {'company': company})

@login_required(login_url='/auth/admin/login/')
def company_delete(request, company_id):
    company = Company.objects.get(id=company_id)
    company.delete()
    return redirect('company-list')

# Placement views

@login_required(login_url='/auth/admin/login/')
def placement_list(request):
    placements = Placement.objects.all()
    return render(request, 'admin_app/placement-list.html', {'placements': placements})

@login_required(login_url='/auth/admin/login/')
def placement_detail(request, placement_id):
    placement = Placement.objects.get(id=placement_id)
    return render(request, 'admin_app/placement-detail.html', {'placement': placement})

@login_required(login_url='/auth/admin/login/')
def placement_add(request):
    if request.method == 'POST':
        image = request.FILES.get('image')
        company_name = request.POST.get('company_name')
        designation = request.POST.get('designation')

        if image and company_name and designation:
            new_placement = Placement(image=image, company_name=company_name, designation=designation)
            new_placement.save()
            return redirect('placement-list')
        
    else:
        return render(request, 'admin_app/placement-add.html')

@login_required(login_url='/auth/admin/login/')
def placement_edit(request, placement_id):
    placement = Placement.objects.get(id=placement_id)

    if request.method == 'POST':
        new_image = request.FILES.get('image')
        if new_image:
            placement.image = new_image
        else:
            new_image = placement.image
        placement.company_name = request.POST.get('company_name')
        placement.designation = request.POST.get('designation')
        placement.save()
        return redirect('placement-list')
        
    else:
        return render(request, 'admin_app/placement-edit.html', {'placement': placement})

@login_required(login_url='/auth/admin/login/')
def placement_delete(request, placement_id):
    placement = Placement.objects.get(id=placement_id)
    placement.delete()
    return redirect('placement-list')

# Gallery views

@login_required(login_url='/auth/admin/login/')
def gallery_list(request):
    galleries = Gallery.objects.all()
    return render(request, 'admin_app/gallery-list.html', {'galleries': galleries})

@login_required(login_url='/auth/admin/login/')
def gallery_detail(request, gallery_id):
    gallery_item = Gallery.objects.get(id=gallery_id)
    return render(request, 'admin_app/gallery-detail.html', {'gallery_item': gallery_item})

@login_required(login_url='/auth/admin/login/')
def gallery_add(request):
    if request.method == 'POST':
        image = request.FILES.get('image')
        shorts_url = request.POST.get('shorts_url')
        yt_url = request.POST.get('yt_url')

        
        gallery = Gallery(
            image=image,
            shorts_url=shorts_url,
            yt_url=yt_url
            )
        gallery.save()
        return redirect('gallery-list')
        
    else:
        return render(request, 'admin_app/gallery-add.html')

@login_required(login_url='/auth/admin/login/')
def gallery_edit(request, gallery_id):
    gallery_item = Gallery.objects.get(id=gallery_id)

    if request.method == 'POST':
        image = request.FILES.get('image')

        if image:
            gallery_item.image = image
            gallery_item.save()
            return redirect('gallery-list')
        
    else:
        return render(request, 'admin_app/gallery-edit.html', {'gallery_item': gallery_item})

@login_required(login_url='/auth/admin/login/')
def gallery_delete(request, gallery_id):
    gallery_item = Gallery.objects.get(id=gallery_id)
    gallery_item.delete()
    return redirect('gallery-list')
