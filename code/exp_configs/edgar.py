# Each experiment is a list of dictionaries, they are excuted sequentially in a workstation or in parallel in a cluster
EXP_GROUPS = {'AWSDR_SDx2_edgar': [{"dataset": { 
                                "lr_type": "LR_bicubic",
                                "data_dir": "/mnt/datasets/public/research/pau/superresolution/",
                                "data_train": "DIV2K",
                                "data_test": "Set5",
                                "data_range": "1-800/801-805",
                                "ext": "img",
                                "scale": [2],
                                "patch_size": 96,
                                "rgb_range": 255,
                                "n_colors": 3,
                                "chop": True,
                                "no_augment": False,
                                },
                        "backbone": {
                            "name": "AWSRN",
                            "act": "relu",
                            "pre_train": None,
                            "extend": None,
                            "n_resblocks": 1,
                            "n_awru": 4,
                            "n_feats": 16,
                            "block_feats": 128,
                            "res_scale": 1,
                            "shift_mean": True,
                            "dilation": False,
                            "precision": "single",
                            "self_ensemble": False,
                        },
                        "model": "kornia_trainer",
                        "test_every": 1000, # 1000
                        "epochs": 300,
                        "ngpu": 2,
                        "batch_size": 16,
                        "split_batch": 1,
                        "test_only": False,
                        "gan_k": 1,
                        "lr": 1e-3,
                        "lr_decay": 200,
                        "period": 1000, #lr restarting period
                        "gamma": 0.5, # lr decay 
                        "optimizer": "ADAM",
                        "loss_l1_weight": 1,
                        "loss_sobel_weight": 0, #TODO edgar
                        "skip_threshold": 1e6, #skipping batch that has large error
                    }]}
