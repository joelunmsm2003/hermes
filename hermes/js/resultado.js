
function Resultado($scope,$http,$filter,$routeParams,$location,$localStorage) {


    $scope.calculo = function (data) {


            var todo = {
                monto:$routeParams,
                data:data
            }


            $http({
            url: host+"/tasaadmin/",
            data: todo,
            method: 'POST',
         
            }).
            success(function(data) {

            console.log('Admin........',data)

                    
                $scope.model.tasahdi = data[0]['tasahdi']
                $scope.model.tasapositiva = data[3]['tasapositiva']
                $scope.model.tasamapfre = data[1]['tasamapfre']
                $scope.model.tasapacifico = data[2]['tasapacifico']
                $scope.model.tasarimac = data[4]['tasarimac']

                $scope.hdi = data[0]['hdi']
                $scope.positiva = data[3]['positiva']
                $scope.mapfre = data[1]['mapfre']
                $scope.pacifico = data[2]['pacifico']
                $scope.rimac = 77777777

                $scope.phdisubtotal = data[0]['phdisubtotal']
                $scope.positivasubtotal = data[3]['positivasubtotal']
                $scope.mapfresubtotal = data[1]['mapfresubtotal']
                $scope.pacificosubtotal = data[2]['pacificosubtotal']
                $scope.rimacsubtotal = data[4]['rimacsubtotal']

                $scope.phditotal = data[0]['phditotal']
                $scope.positivatotal = data[3]['positivatotal']
                $scope.mapfretotal = data[1]['mapfretotal']
                $scope.pacificototal = data[2]['pacificototal']
                $scope.rimactotal = data[4]['rimactotal']

                /*Pdf Genera*/

                $scope.pdf = {}



                $scope.pdf.tasahdi = data[0]['tasahdi']
                $scope.pdf.tasapositiva = data[3]['tasapositiva']
                $scope.pdf.tasamapfre = data[1]['tasamapfre']
                $scope.pdf.tasapacifico = data[2]['tasapacifico']
                $scope.pdf.tasarimac = data[4]['tasarimac']

                $scope.pdf.hdi = data[0]['hdi']
                $scope.pdf.positiva = data[3]['positiva']
                $scope.pdf.mapfre = data[1]['mapfre']
                $scope.pdf.pacifico = data[2]['pacifico']
                $scope.pdf.rimac = data[4]['rimac']

                $scope.pdf.phdisubtotal = data[0]['phdisubtotal']
                $scope.pdf.positivasubtotal = data[3]['positivasubtotal']
                $scope.pdf.mapfresubtotal = data[1]['mapfresubtotal']
                $scope.pdf.pacificosubtotal = data[2]['pacificosubtotal']
                $scope.pdf.rimacsubtotal = data[4]['rimacsubtotal']

                $scope.pdf.phditotal = data[0]['phditotal']
                $scope.pdf.positivatotal = data[3]['positivatotal']
                $scope.pdf.mapfretotal = data[1]['mapfretotal']
                $scope.pdf.pacificototal = data[2]['pacificototal']
                $scope.pdf.rimactotal = data[4]['rimactotal']

                $http({

                    url: host+"/recibetasas/",
                    data: $scope.pdf,
                    method: 'POST',

                    })

            })


    }

    if($localStorage.token){ 

	    $http.get(host+"/perfil/").success(function(response) {

            console.log('perfil',response)

            $scope.perfil = response

            });


 }


    $scope.order_id = $routeParams.orderId;

    $scope.uso = $routeParams.uso

    $scope.tipo = $routeParams.tipo

    $scope.modalidad = $routeParams.modalidad

    $scope.anio = $routeParams.anio

    $scope.monto = $routeParams.monto

    $scope.riesgo = $routeParams.riesgo

    $scope.categoria = $routeParams.categoria

    $scope.programa = $routeParams.programa

    $scope.ubicacion = $routeParams.ubicacion

    $scope.categoria = $routeParams.categoria

    $scope.modelo = $routeParams.modelo

    $scope.absUrl = $location.absUrl();

    console.log('$scope.riesgo',$scope.riesgo)

    $scope.model = {}
    $scope.datamodel = {}

    $http.get(host+"/programas/").success(function(response) {$scope.programas = response;
    
    console.log('Programas',$scope.programas)
    $scope.model.programa = $scope.programas[3]

    //$scope.programa($scope.model)


    });

    //3 HDI 4 Mapfre 2 Pacifico 1 Positiva 5 Rimac

  $http.get(host+"/asegprogram/"+1+"/").success(function(response) {$scope.programaspositiva = response;

    $scope.model.programap = $scope.programaspositiva[0]

  });
  $http.get(host+"/asegprogram/"+2+"/").success(function(response) {$scope.programaspacifico = response;});
  $http.get(host+"/asegprogram/"+3+"/").success(function(response) {$scope.programashdi = response;});
  $http.get(host+"/asegprogram/"+4+"/").success(function(response) {$scope.programasmapfre = response;

      console.log('Mapgre programs',$scope.programasmapfre)

      $scope.model.programam = $scope.programasmapfre[2]

  });
  $http.get(host+"/asegprogram/"+5+"/").success(function(response) {$scope.programasrimac = response;

    $scope.model.programar = $scope.programasrimac[4]

  });


  $http.get(host+"/getgps/"+$scope.modelo+"/").success(function(response) {

    console.log('GPS',response)


      $http({
        
        url: host+"/recibegps/",
        data: response,
        method: 'POST',
     
        })

    $scope.gps = response

  });






    $http.get(host+"/datosfiltro/"+$scope.order_id+"/").success(function(response) {$scope.cliente = response[0];

        console.log('cliente',$scope.cliente)

        var f = new Date();

          $http({

            url: host+"/recibecliente/",
            data: response,
            method: 'POST',
         
            })


        $scope.cliente.fecha = f.getDate() + "/" + (f.getMonth() +1) + "/" + f.getFullYear()

    });

    $scope.mafe = 4
    $scope.posi = 25
    $scope.ri = 18
    $scope.pa = ''

    $scope.programa = $scope.mafe+'z'+$scope.ri+'z'+$scope.posi+'z'+$scope.pa

    $scope.programamapfre = function (data) {

        $scope.mafe = data.programam.id_prog 

        console.log($scope.mafe)

        console.log($scope.posi)

        $scope.programa = $scope.mafe+'z'+$scope.ri+'z'+$scope.posi+'z'+$scope.pa

        console.log('programa',$scope.programa)

        $http.get(host+"/cobertura/"+$scope.order_id+'/'+$scope.uso+'/'+$scope.anio+'/'+$scope.modalidad+'/'+$scope.programa+'/'+$scope.modelo+"/").success(function(response) {

            $scope.cobertura = response;

            $http({
            url: host+"/recibecoberturas/",
            data: $scope.cobertura,
            method: 'POST',
         
            })

        });

         $http.get(host+"/deducible/"+$scope.order_id+'/'+$scope.uso+"/"+$scope.anio+'/'+$scope.modalidad+'/'+$scope.programa+'/'+$scope.modelo+"/").success(function(response) {

            $scope.deducible = response;

              $http({
            url: host+"/recibededucibles/",
            data: $scope.deducible,
            method: 'POST',
         
            })

        });

    }

    $scope.programarimac = function (data) {

        $scope.ri = data.programar.id_prog
        console.log($scope.ri)


        console.log($scope.posi)

        $scope.programa = $scope.mafe+'z'+$scope.ri+'z'+$scope.posi+'z'+$scope.pa

        console.log('programa',$scope.programa)

        $http.get(host+"/cobertura/"+$scope.order_id+'/'+$scope.uso+'/'+$scope.anio+'/'+$scope.modalidad+'/'+$scope.programa+'/'+$scope.modelo+"/").success(function(response) {

            $scope.cobertura = response;

            $http({
            url: host+"/recibecoberturas/",
            data: $scope.cobertura,
            method: 'POST',
         
            })

        });

         $http.get(host+"/deducible/"+$scope.order_id+'/'+$scope.uso+"/"+$scope.anio+'/'+$scope.modalidad+'/'+$scope.programa+'/'+$scope.modelo+"/").success(function(response) {

        $scope.deducible = response;

          $http({
            url: host+"/recibededucibles/",
            data: $scope.deducible,
            method: 'POST',
         
            })

        });

    }

    $scope.programapositiva = function (data) {

      

        $scope.posi = data.programap.id_prog

        console.log($scope.posi)

        $scope.programa = $scope.mafe+'z'+$scope.ri+'z'+$scope.posi+'z'+$scope.pa

        console.log('programa',$scope.programa)

        $http.get(host+"/cobertura/"+$scope.order_id+'/'+$scope.uso+'/'+$scope.anio+'/'+$scope.modalidad+'/'+$scope.programa+'/'+$scope.modelo+"/").success(function(response) {

            $scope.cobertura = response;

            $http({
            url: host+"/recibecoberturas/",
            data: $scope.cobertura,
            method: 'POST',
         
            })

        });

         $http.get(host+"/deducible/"+$scope.order_id+'/'+$scope.uso+"/"+$scope.anio+'/'+$scope.modalidad+'/'+$scope.programa+'/'+$scope.modelo+"/").success(function(response) {

        $scope.deducible = response;

          $http({
            url: host+"/recibededucibles/",
            data: $scope.deducible,
            method: 'POST',
         
            })

        });

    }

    $scope.programapacifico = function (data) {

        $scope.pa = data.programapa.id_prog
        console.log($scope.pa)


        console.log($scope.posi)

        $scope.programa = $scope.mafe+'z'+$scope.ri+'z'+$scope.posi+'z'+$scope.pa

        console.log('programa',$scope.programa)

        $http.get(host+"/cobertura/"+$scope.order_id+'/'+$scope.uso+'/'+$scope.anio+'/'+$scope.modalidad+'/'+$scope.programa+'/'+$scope.modelo+"/").success(function(response) {

            $scope.cobertura = response;

            $http({
            url: host+"/recibecoberturas/",
            data: $scope.cobertura,
            method: 'POST',
         
            })

        });

         $http.get(host+"/deducible/"+$scope.order_id+'/'+$scope.uso+"/"+$scope.anio+'/'+$scope.modalidad+'/'+$scope.programa+'/'+$scope.modelo+"/").success(function(response) {

        $scope.deducible = response;

          $http({
            url: host+"/recibededucibles/",
            data: $scope.deducible,
            method: 'POST',
         
            })

        });

    }



    $scope.uploadpdf = function () {


            $http({
            url: host+"/pdfx/",
            data: $scope.absUrl,
            method: 'POST',
         
            }).
            success(function(data) {

             window.open('http://cotizador.hermes.pe:8000/pdfout', "_blank");

            })


    }

        $http.get(host+"/cobertura/"+$scope.order_id+'/'+$scope.uso+'/'+$scope.anio+'/'+$scope.modalidad+'/'+$scope.programa+'/'+$scope.modelo+"/").success(function(response) {

            $scope.cobertura = response;

            $http({
            url: host+"/recibecoberturas/",
            data: $scope.cobertura,
            method: 'POST',
         
            })

            $http({
            url: host+"/pdfx/",
            data: $scope.absUrl,
            method: 'POST',
         
            }).
            success(function(data) {


            })

        });

        console.log('Deducible.............')


        $http.get(host+"/servic/"+$scope.order_id+'/'+$scope.uso+"/"+$scope.anio+'/'+$scope.modalidad+'/'+$scope.programa+"/").success(function(response) {

        $scope.servic = response;

        console.log('servic HDI',$scope.servic)

        $http({
            url: host+"/recibeservicios/",
            data: $scope.servic,
            method: 'POST',
         
            })

        });

        /*
        $http.get(host+"/financ/").success(function(response) {

        $scope.financ = response;

        console.log('Financiamiento',$scope.financ)

        });

*/


     $http.get(host+"/deducible/"+$scope.order_id+'/'+$scope.uso+"/"+$scope.anio+'/'+$scope.modalidad+'/'+$scope.programa+'/'+$scope.modelo+"/").success(function(response) {

        $scope.deducible = response;

          $http({
            url: host+"/recibededucibles/",
            data: $scope.deducible,
            method: 'POST',
         
            })

        });


    console.log('Data...',$routeParams)

    $scope.model = {}



    $http({

        url: host+"/primaneta/",
        data: $routeParams,
        method: 'POST',

    }).
    success(function(data) {

        console.log(data)

        $scope.model.tasahdi = data[0]['tasahdi']
        $scope.model.tasapositiva = data[3]['tasapositiva']
        $scope.model.tasamapfre = data[1]['tasamapfre']
        $scope.model.tasapacifico = data[2]['tasapacifico']
        $scope.model.tasarimac = data[4]['tasarimac']

        $scope.hdi = data[0]['hdi']
        $scope.positiva = data[3]['positiva']
        $scope.mapfre = data[1]['mapfre']
        $scope.pacifico = data[2]['pacifico']
        $scope.rimac = data[4]['rimac']

        $scope.phdisubtotal = data[0]['phdisubtotal']
        $scope.positivasubtotal = data[3]['positivasubtotal']
        $scope.mapfresubtotal = data[1]['mapfresubtotal']
        $scope.pacificosubtotal = data[2]['pacificosubtotal']
        $scope.rimacsubtotal = data[4]['rimacsubtotal']

        $scope.phditotal = data[0]['phditotal']
        $scope.positivatotal = data[3]['positivatotal']
        $scope.mapfretotal = data[1]['mapfretotal']
        $scope.pacificototal = data[2]['pacificototal']
        $scope.rimactotal = data[4]['rimactotal']

                /*Pdf Genera*/

        $scope.pdf = {}



        $scope.pdf.tasahdi = data[0]['tasahdi']
        $scope.pdf.tasapositiva = data[3]['tasapositiva']
        $scope.pdf.tasamapfre = data[1]['tasamapfre']
        $scope.pdf.tasapacifico = data[2]['tasapacifico']
        $scope.pdf.tasarimac = data[4]['tasarimac']

        $scope.pdf.hdi = data[0]['hdi']
        $scope.pdf.positiva = data[3]['positiva']
        $scope.pdf.mapfre = data[1]['mapfre']
        $scope.pdf.pacifico = data[2]['pacifico']
        $scope.pdf.rimac = data[4]['rimac']

        $scope.pdf.phdisubtotal = data[0]['phdisubtotal']
        $scope.pdf.positivasubtotal = data[3]['positivasubtotal']
        $scope.pdf.mapfresubtotal = data[1]['mapfresubtotal']
        $scope.pdf.pacificosubtotal = data[2]['pacificosubtotal']
        $scope.pdf.rimacsubtotal = data[4]['rimacsubtotal']

        $scope.pdf.phditotal = data[0]['phditotal']
        $scope.pdf.positivatotal = data[3]['positivatotal']
        $scope.pdf.mapfretotal = data[1]['mapfretotal']
        $scope.pdf.pacificototal = data[2]['pacificototal']
        $scope.pdf.rimactotal = data[4]['rimactotal']

        $http({

            url: host+"/recibetasas/",
            data: $scope.pdf,
            method: 'POST',

            })






    })

       




    $http({

        url: host+"/enviaemail/",
        data: $routeParams,
        method: 'POST',

    }).
    success(function(data) {

        console.log(data)


    })



    $http({

        url: host+"/fiiiii/",
        data: $routeParams,
        method: 'POST',

    }).
    success(function(data) {

        console.log(data)

        $scope.financ = data;

         $http({

                url: host+"/recibefinanciamiento/",
                data: data,
                method: 'POST',

            })


    })
    






}

