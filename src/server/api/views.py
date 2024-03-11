# compiler and interpreter api
##from src.compilers.linear_algebra_interpreter.parser import lalg_parser
#from src.compilers.linear_algebra_interpreter.interpreter import evaluate
#from src.compilers.linear_algebra_to_c.parser import cparser
#from src.compilers.linear_algebra_to_c.ast_to_lalg import ast_to_lalg
#from src.compilers.linear_algebra_to_c.lalg_to_c import lalg_to_c
from src.compilers.scm_interpreter.parser import scmparser 
from src.compilers.scm_interpreter.interp import interp
# models
from .models import (
    LinearAlgebraCompiler,
    LinearAlgebraInterpreter,
    SchemeInterpreter,
    )
# djangorestframework api
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
# django api
from django.contrib.auth import (
    authenticate,
    login,
    get_user_model,
    )

# forms
from .forms import (
    CompilerForm,
    UserRegistrationForm,
    UploadSchemeFile,
    )
# serializers
from .serializers import (
    LinearAlgebraInterpSerializer,
    LinearAlgebraCompilerSerializer,
    SchemeInterpSerializer,
    )
import io
User = get_user_model()

@api_view(['POST'])
def register(request):
    form = UserRegistrationForm(request.POST)
    if form.is_valid():
        new_user = form.save(commit=False)
        data = form.cleaned_data
        new_user.set_password(data['password'])
        new_user.save()

        return Response({'account':'created'})

    return Response({'form':'invalid'})

@api_view(['POST'])
def login(request):
    form = LoginForm(request.POST)
    if form.is_valid():
        data = form.cleaned_data
        username = data['username']
        password = data['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return Response({"login": "successful"})
        return Response({"create": "account"})
    return Response({'form': 'invalid'})

@api_view(['POST'])
@login_required(login_url='/api/login')
def scheme_interpreter(request):
    form = CompilerForm(request.POST)
    if form.is_valid():
        data = form.cleaned_data
        exp = data['input_expression']
        parsed_exp = scmparser.parse(exp)
        evaluation = interp(parsed_exp)
        scm_model = SchemeInterpreter(input_expression=data['input_expression'], output_expression=evaluation)
        scm_model.save()
        user = request.user
        user.scm_interp_exps.add(scm_model)
        serializer = SchemeInterpSerializer(scm_model)
        return Response(serializer.data)
    return Response({'form':'invalid'})

@api_view(['POST'])
@login_required(login_url='/api/login')
def evaluate_scm_from_file(request):
    form = UploadSchemeFile(request.POST, request.FILES)
    print("form data:", request.POST)
    print("files:", request.FILES)
    #if form.is_valid():
    scm_file = request.FILES['scm_file']
    print(type(scm_file))
    scm_exp = scm_file.file
    print(type(scm_exp))
    bytes_data = scm_exp
   # print(type(bytes_data))
    scm_exp = bytes_data.read().decode('utf-8')
   # decoded_text = bytes_data.decode('utf-8')
    parsed_exp = scmparser.parse(scm_exp)
    evaluation = interp(parsed_exp)
    scm_model = SchemeInterpreter(input_expression=scm_exp, output_expression=evaluation)
    scm_model.save()
    user = request.user
    user.scm_interp_exps.add(scm_model)
    serializer = SchemeInterpSerializer(scm_model)
    return Response(serializer.data)
    ###return Response({"invalid": "form"})

@api_view(['GET'])
@login_required(login_url='/api/login')
def scheme_expressions(request):
    usr = request.user
    exps = usr.scm_interp_exps.all()
    serializer = SchemeInterpSerializer(exps, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@login_required(login_url='/api/login')
def scheme_expression(request, id):
    usr = request.user
    exp = usr.scm_interp_exps.get(id=id)
    serializer = SchemeInterpSerializer(exp)
    return Response(serializer.data)

"""
@api_view(['POST'])
@login_required(login_url='/api/login')
def linear_algebra_compiler(request):
    form = CompilerForm(request.POST)
    if form.is_valid():
        data = form.cleaned_data
        exp = data['input_expression']
        parsed_exp = cparser.parse(exp)
        ir = ast_to_lalg(parsed_exp)
        
        compilation = lalg_to_c(parsed_exp)
        lalg_model = LinearAlgebraCompiler(input_expression=data['input_expression'], output_expression=evaluation)
        lalg_model.save()
        user = request.user
        user.lalg_compile_exps.add(lalg_model)
        serializer = LinearAlgebraCompilerSerializer(lalg_model)
        return Response(serializer.data)
    return Response({'form':'invalid'})
        
"""
"""
@api_view(['POST'])
@login_required(login_url='/api/login')
def linear_algebra_interp(request):
    form = CompilerForm(request.POST)
    if form.is_valid():
        data = form.cleaned_data
        exp = data['input_expression']
        parsed_exp = lalg_parser.parse(exp)
        print(parsed_exp)
        evaluation = str(evaluate(parsed_exp))
        print(evaluation)
        lalg_model = LinearAlgebraInterpreter(input_expression=data['input_expression'], output_expression=evaluation)
        lalg_model.save()
        user = request.user
        user.lalg_interp_exps.add(lalg_model)
        serializer = LinearAlgebraInterpSerializer(lalg_model)
        return Response(serializer.data)
    return Response({'form':'invalid'})
        
"""
