# example_ROS_Python_Vrep_Fuzzy

Esse pacote ROS tem por finalidade desenvolver um controle Fuzzy para que o Robô desvie do obstáculo. O controle desenvolvido apenas manipula a velocidade angular aplicada ao robô, a velocidade Linear é constante e passível de alteração no código.  

# Arvore de arquivos 

* Scripts/init.py: Arquivo principal, contém a manipulação dos dados e aplica o Fuzzy;  
* Scripts/Fuzzy_angular.py: Possui todo o código referente ao Fuzzy. Fuzzy simples, uma entrada e uma saída. Suas entras e saídas podem ser vistas a seguir. 
![alt text](https://github.com/marco-teixeira/tutorial_examples_ROS/blob/master/Python/example_ROS_Python_Vrep_Fuzzy/figure/fuzzy.png) 
* vrep: Pasta com as cenas utilizadas. Possui cena tanto para o ROS-plugin quanto para o ROS-interface.  
# Instalando dependências  

É necessário instalar o pacote skfuzzy 

  $ sudo pip install scikit-fuzzy 

# Contribuições 

* Função em Python para obter dados do tipo Lidar "getLidar"; 
* Exemplo simples de uso da ferramenta skfuzzy; 
* Exemplo simples de processamento de pontos 3D. Neste exemplo, é calculado a distância euclidiana entre todos os pontos capturados pelo sensor e o Robô.  


# Como usar 

Para rodar o código, execute a cena e então rode o comando: 

  $ roslaunch example_ROS_Python_Vrep_Fuzzy start.launch  

Ou 

  $ rosrun example_ROS_Python_Vrep_Fuzzy init.py 

Caso nenhum dos dois funcionar, lembre-se de dar permissão de execução para o arquivo Python.  

 
