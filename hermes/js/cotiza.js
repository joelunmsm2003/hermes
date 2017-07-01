
function Cotiza($scope,$http,$filter,$location,$localStorage) {

    $scope.riesgo = 8

    $scope.categoria = 1

    $scope.ubicL= true

    $scope.ubicP= true


      function urlBase64Decode(str) {
        var output = str.replace('-', '+').replace('_', '/');
        switch (output.length % 4) {
            case 0:
                break;
            case 2:
                output += '==';
                break;
            case 3:
                output += '=';
                break;
            default:
                throw 'Illegal base64url string!';
        }
        return window.atob(output);
    }


    function getUserFromToken() {
        var token = $localStorage.token;
        var user = {};
        if (typeof token !== 'undefined') {
            var encoded = token.split('.')[1];
            user = JSON.parse(urlBase64Decode(encoded));
        }
        return user;
    }

    console.log('User',getUserFromToken().user_id)

    $scope.user = getUserFromToken().user_id

    








    $scope.antiguedad = [{
    id: 1,
    label: 'Nuevo',
   
    }, {
    id: 2,
    label: 'Usado',
  
    }];

    $scope.est_antiguedad = 'False'

    $scope.model = {}

    console.log($scope.antiguedad)

    $scope.data = function (todo) {

        console.log('hdhdhd',todo)


    }

    // $scope.antig = function (todo) {

    //     console.log(todo)

    //     if($scope.model.modelo.id_modelo == undefined){


    //         console.log('ksksksk')
    //     }



    //     id_modelo = $scope.model.modelo.id_modelo



    //     if(todo.antiguedad.label == 'Usado'){

    //         $http.get(host+"/precio/"+id_modelo+'/'+todo.anio.anio_antig).success(function(response) {

    //         console.log('precio',response)

           

    //         $http.get(host+"/preciodreprecio/"+response).success(function(response) {

    //         $scope.precio = response

    //         });

    //         });



          
    //     }

    //     if(todo.antiguedad.label == 'Nuevo'){

    //         //$scope.CurrentDate = new Date()

    //         //anio = $filter('date')($scope.CurrentDate, 'yyyy')

            
    //         $http.get(host+"/precio/"+id_modelo+'/'+todo.anio.anio_antig).success(function(response) {

    //         console.log('precio',response)

    //         $scope.precio = response

    //         });






    //     }

    // }


    $scope.logear = function (todo) {

        console.log

       
        $http({
        url: host+"/logearse/",
        data: todo,
        method: 'POST',
     
        }).
        success(function(data) {
          
          console.log(data)

        })

    }

    $http.get(host+"/estadologin/").success(function(response) {$scope.estadologin = response;

      
    });


    $http.get(host+"/marca/").success(function(response) {$scope.marca = response;

      
    });

    $http.get(host+"/uso/").success(function(response) {$scope.uso = response;

      
    });

    $http.get(host+"/anio/").success(function(response) {$scope.anio = response;


        console.log($scope.anio[12])
        //$scope.model.anio = $scope.anio[0]

      
    });


    $http.get(host+"/timon/").success(function(response) {$scope.timon = response;

      
    });

    $http.get(host+"/modalidad/").success(function(response) {$scope.modalidad = response;

        $scope.model.modalidad= $scope.modalidad[1]

      
    });

    //console.log($scope.items);




    $scope.obtenermodelo = function (data) {

       
    $http.get(host+"/modelo/"+data.marca.id_marca+'/').success(function(response) {

        $scope.modelo = response

        console.log($scope.modelo)

      
    });

    }

    $scope.evaluaanio=function(data){

        console.log('aniooooo',data)

        if(data.id_anio<28){

            $scope.showantiguedad = false


        }
        else{

            $scope.showantiguedad = true
        }
    }


       
    $scope.obtenerclase = function (data) {
    
        $http.get(host+"/claseModelo/"+data.modelo.id_modelo+'/').success(function(response) {

            $scope.claseModelo = response

            console.log('claseModelo',response)

            $scope.vari= $scope.claseModelo[0].id

            $http.get(host+"/riesgomodelo/"+$scope.vari+'/').success(function(response) {

            console.log("/riesgomodelo/",response)

            varx = ''

            for (var i = 0; i < response.length; i++) {

                varx = varx +response[i].aseguradora__name_asegurad+'aseg'+response[i].id_riesg_id+'riesg'
            }

      


            $scope.riesgo = varx

            if (varx==''){

                $scope.riesgo = 3
            }



           
        });

       

      
    });





    }

    $scope.programa = 3

    $scope.ubicacion = 1


    $scope.obtenerprecio = function (data) {

        console.log('obtenerprecio',data)

  

        $http.get(host+"/precio/"+$scope.model.claseModelo.id_modelo+'/'+data.anio.anio_antig+'/').success(function(response) {

        console.log('precio',response)

        $scope.precio = response
             
        });


    }


        $scope.obteneruso = function (data) {

        

  

        $http.get(host+"/usos/"+$scope.model.claseModelo.id_tipo).success(function(response) {

            console.log('response',response)

        $scope.uso = response
             
        });


    }



$scope.items = [{
id: 1,
label: 'Lima'
}, {
id: 2,
label: 'Provincia'
}];

$scope.selected = $scope.items[0];





        $scope.saveContact = function (model,precio,check,ubicP,ubicL) {





       console.log('SAVE',model)

       modelo = model.modelo.id_modelo

       tipo = model.claseModelo.id_tipo

       marca = model.marca.id_marca


        var todo={

            add: "Guardar",
            dato: model,
            precio:precio,
            ubicL:ubicL,
            ubicP:ubicP,
            check:check,
            modelo:modelo,
            done:false
        }



        if ($scope.check== 1){

            $scope.model.statuscheck = 1
        }
        else{
            $scope.model.statuscheck = 0

        }

        console.log('check',$scope.model.check)
        

        if ($scope.ubicL== 1){

            $scope.model.statusubicL = 1
        }
        else{
            $scope.model.statusubicL = 0

        }        

        console.log('ubicL',$scope.model.ubicL)

        if ($scope.ubicP== 1){

            $scope.model.statusubicP = 1
        }
        else{
            $scope.model.statusubicP = 0

        }  
        
        console.log('ubicP',$scope.model.ubicP)

        $http({
        url: host+"/cotiSave/",
        data: todo,
        method: 'POST',
     
        }).
        success(function(data) {



      /// Trae Programas

      console.log('preciooooo',$scope.precio)

      $http.get(host+"/asegprogram/"+4+"/"+model.modelo.id_modelo+'/'+model.uso+'/'+marca+'/'+tipo+'/'+$scope.precio).success(function(response) {

        console.log('prog4',response)

        $scope.pm = response; $scope.pm = $scope.pm[0].id_prog

        $http.get(host+"/asegprogram/"+5+"/"+model.modelo.id_modelo+'/'+model.uso+'/'+marca+'/'+tipo+'/'+$scope.precio).success(function(response) {

            console.log(response,'5.....'); 
            $scope.pr = response; 
            $scope.pr = $scope.pr[0].id_prog

            console.log('pm',$scope.pm)

            console.log('pr',$scope.pr)

            if(!$scope.pr){

                $scope.pr=666
            }

             programita = $scope.pm+'z'+$scope.pr+'z3z'

            console.log(programita)

        $location.url('/resultado/'+data+'/'+model.uso+'/'+model.anio.id_anio+'/'+model.modalidad.id_modalidad+'/'+programita+'/'+model.modelo.id_modelo+'/'+$scope.precio+'/'+tipo+'/'+marca)
            


        });





    });
     
      

       

      })


        
    };


}

