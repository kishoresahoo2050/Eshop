from django.shortcuts import HttpResponseRedirect





def Authenticate_Middel(get_respone):

    def middleware(request):
        if not request.session.get('user_id'):
            return HttpResponseRedirect('/logins/')
      
      
        respo = get_respone(request)

        return respo
    return middleware