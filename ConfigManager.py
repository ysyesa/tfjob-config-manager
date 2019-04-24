class ConfigManager:
    def __init__(self, filename, special_keywords=None):
        self.file = open(filename, "w")
        self.special_keywords = ["containers", "env"] if special_keywords is None else special_keywords
        pass

    def generate_config_file(self):
        self.__generate_config_file(self.CONFIG, 0, False)

    def set_tfjob_name(self, name):
        self.CONFIG[5][1] = name

    def set_tfjob_master_image(self, image):
        self.CONFIG[7][1][1][3][1][1][3] = image

    def set_tfjob_master_replica(self, num):
        self.CONFIG[7][1][1][1] = num

    def set_tfjob_worker_image(self, image):
        self.CONFIG[7][1][3][3][1][1][3] = image

    def set_tfjob_worker_replica(self, num):
        self.CONFIG[7][1][3][1] = num

    def set_tfjob_ps_image(self, image):
        self.CONFIG[7][1][5][3][1][1][3] = image

    def set_tfjob_ps_replica(self, num):
        self.CONFIG[7][1][5][1] = num

    def set_tfjob_env_variable(self, key, value):
        self.CONFIG[7][1][1][3][1][1][5][1] = key
        self.CONFIG[7][1][1][3][1][1][5][3] = value
        self.CONFIG[7][1][3][3][1][1][5][1] = key
        self.CONFIG[7][1][3][3][1][1][5][3] = value
        self.CONFIG[7][1][5][3][1][1][5][1] = key
        self.CONFIG[7][1][5][3][1][1][5][3] = value

    def __generate_config_file(self, config, order, is_special_keyword):
        for index in range(len(config)):
            # Writing key
            if index % 2 == 0:
                for i in range(2 * order):
                    self.file.write(" ")
                if is_special_keyword:
                    self.file.write("- ")
                    is_special_keyword = False
                    order = order + 1
                self.file.write(config[index] + ": ")

            # Writing value
            else:
                if isinstance(config[index], list):
                    self.file.write("\n")
                    self.__generate_config_file(
                        config[index], order + 1,
                        True if config[index - 1] in self.special_keywords else False
                    )
                else:
                    self.file.write(config[index] + "\n")

    CONFIG = [
        "apiVersion",
        "kubeflow.org/v1alpha2",
        "kind",
        "TFJob",
        "metadata",
        [
            "name",
            "dist-tf-mnist"
        ],
        "spec",
        [
            "tfReplicaSpecs",
            [
                "Master",
                [
                    "replicas",
                    "1",
                    "template",
                    [
                        "spec",
                        [
                            "containers",
                            [
                                "name",
                                "tensorflow",
                                "image",
                                "ysyesa/dist-tf-mnist",
                                "env",
                                [
                                    "name",
                                    "TOTAL_EPOCH&CURRENT_EPOCH",
                                    "value",
                                    "999&111"
                                ]
                            ]
                        ]
                    ]
                ],
                "Worker",
                [
                    "replicas",
                    "1",
                    "template",
                    [
                        "spec",
                        [
                            "containers",
                            [
                                "name",
                                "tensorflow",
                                "image",
                                "ysyesa/dist-tf-mnist",
                                "env",
                                [
                                    "name",
                                    "TOTAL_EPOCH&CURRENT_EPOCH",
                                    "value",
                                    "999&111"
                                ]
                            ]
                        ]
                    ]
                ],
                "PS",
                [
                    "replicas",
                    "1",
                    "template",
                    [
                        "spec",
                        [
                            "containers",
                            [
                                "name",
                                "tensorflow",
                                "image",
                                "ysyesa/dist-tf-mnist",
                                "env",
                                [
                                    "name",
                                    "TOTAL_EPOCH&CURRENT_EPOCH",
                                    "value",
                                    "999&111"
                                ]
                            ]
                        ]
                    ]
                ]
            ]
        ]
    ]
