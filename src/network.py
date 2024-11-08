from flask import Flask, Response
from mininet.node import RemoteController
from mininet.topo import Topo
from typing import List

from qos import FlowManager
from monitor import MonitorService
from information import RoutineResults, Display, Manual

class ActionDirector:
    @staticmethod
    def __read_args() -> dict:
        pass

    @staticmethod
    def create_network() -> None:
        """
            Inicializa um controlador de serviços num novo processo
        """
        sc = ServicesController()
        # Abre um processo e chama o método start
        sc.start()
        # Informa sobre o status da operação

    @staticmethod
    def destroy_network() -> None:
        """
            Executa as rotinas para a destruição da rede criada.
        """
        ActionDirector.__get_service_controller_process()
        sc.destroy()

    @staticmethod
    def create_policy() -> None:
        """
            Recebe as informações da política por parâmetros CLI
            e executa as rotinas de criação de uma nova política.
        """
        ActionDirector.__get_service_controller_process()
        pass

    @staticmethod
    def update_policy() -> None:
        """
            Recebe as informações da política por parâmetros CLI
            e executa as rotinas de atualização de políticas.
        """
        ActionDirector.__get_service_controller_process()
        pass

    @staticmethod
    def remove_policy() -> None:
        """
            Recebe as informações da política por parâmetros CLI
            e executa as rotinas de remoção de políticas.
        """
        ActionDirector.__get_service_controller_process()
        pass

    @staticmethod
    def show_network_state() -> None:
        """
            Executa rotinas de recuperação de informações sobre
            a rede instanciada, as políticas ativas e o monitoramento
        """
        ActionDirector.__get_service_controller_process()
        pass

    @staticmethod
    def show_manual() -> None:
        """
            Exibe informações do manual do controlador com um nível de
            detalhes a depender do especificado por parâmetros CLI.
        """
        pass

class Api:
    app = Flask(__name__)

class ServicesController:
    def __init__(self):
        self.__config = None # read_config
        self.__topo_manager = TopoManager()
        self.__flow_manager = FlowManager()
        self.__monitor_service = MonitorService()

    @Api.app.route("/start")
    def start(self) -> str:
        """
            Inicializa o editor de topologia e gera a topologia desejada,
            se houver sucesso na geração inicializa o serviço de monitoramento.
        """
        return "ok"

    @Api.app.route("/destroy")
    def destroy(self) -> Response:
        """
            Executa a rotina de desalocação de recursos da rede.
        """
        self.__topo_manager.destroy()

    @Api.app.route("/get_statistics")
    def get_statistics(self) -> Response:
        """
            Executa a rotina de recuperação de informações da rede.
        """
        pass

    @Api.app.route("/manage_policy")
    def manage_policy(self) -> Response:
        pass

    @Api.app.route("/capture_alerts")
    def capture_alerts(self, policy_data: dict) -> Response:
        pass

class TopoManager:
    def __init__(self):
        self.__net: Mininet = None

    def __load_network(self) -> RoutineResults:
        """
            Procura pelo arquivo JSON de topologia definida no diretório ASSETS_DIR,
            interpreta cada valor no arquivo e inicializa o gerenciador de topologia.
        """
        topo = Topology()
        controller = Controller.create_controller()
        self.__net = Mininet(topo, controller)

    def generate(self) -> RoutineResults:
        """
            Carrega a topologia desejada.
        """
        psr = self.__load_network()

        if not psr.status:
            # retorna PSR com erro
            pass 

        self.__net.start()

    def destroy(self) -> RoutineResults:
        """
            Desaloca os recursos da topologia instanciada.
        """
        pass

    def report_topology_state(self) -> RoutineResults:
        """
            Recupera informações sobre a topologia instanciada.
        """
        pass

class Topology(Topo):
    def build(self) -> None:
        pass

class Controller(RemoteController):
    CONTROLLER_NAME = "c0"
    CONTROLLER_ADDR = "127.0.0.1"
    OPF_PORT = 6653

    @staticmethod
    def create_controller(
        name: str = CONTROLLER_NAME,
        addr: str = CONTROLLER_ADDR,
        port: int = OPF_PORT
    ) -> RemoteController:
        return RemoteController(
            name,
            ip=addr,
            port=port
        )

