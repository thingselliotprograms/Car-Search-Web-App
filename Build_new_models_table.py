from __future__ import print_function
import mysql.connector

cnx = mysql.connector.connect(user='root',password='soccer',host='localhost',database='elliot_edmunds')
cursor = cnx.cursor()

'''
add_model = ("INSERT INTO new_models "
             "(maker, model, model_year, model_id) "
             "VALUES (%s, %s, %s, %s)")

modelsdict = {
    "makes": [{
        "id": 200002038,
        "name": "Acura",
        "niceName": "acura",
        "models": [{
            "id": "Acura_ILX",
            "name": "ILX",
            "niceName": "ilx",
            "years": [{
                "id": 200713715,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401640361,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Acura_MDX",
            "name": "MDX",
            "niceName": "mdx",
            "years": [{
                "id": 200726800,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 200781960,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Acura_NSX",
            "name": "NSX",
            "niceName": "nsx",
            "years": [{
                "id": 200779937,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Acura_RDX",
            "name": "RDX",
            "niceName": "rdx",
            "years": [{
                "id": 200727186,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401640362,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Acura_RLX",
            "name": "RLX",
            "niceName": "rlx",
            "years": [{
                "id": 200729233,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401676770,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Acura_TLX",
            "name": "TLX",
            "niceName": "tlx",
            "years": [{
                "id": 401583109,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401658802,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }]
    }, {
        "id": 200464140,
        "name": "Alfa Romeo",
        "niceName": "alfa-romeo",
        "models": [{
            "id": "Alfa_Romeo_4C",
            "name": "4C",
            "niceName": "4c",
            "years": [{
                "id": 401630278,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401665445,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Alfa_Romeo_Giulia",
            "name": "Giulia",
            "niceName": "giulia",
            "years": [{
                "id": 200741082,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "FUTURE"]
        }]
    }, {
        "id": 200001769,
        "name": "Aston Martin",
        "niceName": "aston-martin",
        "models": [{
            "id": "Aston_Martin_DB11",
            "name": "DB11",
            "niceName": "db11",
            "years": [{
                "id": 401696107,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW"]
        }, {
            "id": "Aston_Martin_DB9_GT",
            "name": "DB9 GT",
            "niceName": "db9-gt",
            "years": [{
                "id": 401630246,
                "year": 2016,
                "states": ["NEW", "USED"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Aston_Martin_Rapide_S",
            "name": "Rapide S",
            "niceName": "rapide-s",
            "years": [{
                "id": 401632439,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401698011,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Aston_Martin_V12_Vantage_S",
            "name": "V12 Vantage S",
            "niceName": "v12-vantage-s",
            "years": [{
                "id": 401633296,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401699716,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Aston_Martin_V8_Vantage",
            "name": "V8 Vantage",
            "niceName": "v8-vantage",
            "years": [{
                "id": 401627333,
                "year": 2016,
                "states": ["NEW", "USED"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Aston_Martin_Vanquish",
            "name": "Vanquish",
            "niceName": "vanquish",
            "years": [{
                "id": 401631544,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401696095,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }]
    }, {
        "id": 200000001,
        "name": "Audi",
        "niceName": "audi",
        "models": [{
            "id": "Audi_A3",
            "name": "A3",
            "niceName": "a3",
            "years": [{
                "id": 200694130,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401662137,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "FUTURE", "USED"]
        }, {
            "id": "Audi_A3_Sportback_e_tron",
            "name": "A3 Sportback e-tron",
            "niceName": "a3-sportback-e-tron",
            "years": [{
                "id": 200748640,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401662138,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Audi_A4",
            "name": "A4",
            "niceName": "a4",
            "years": [{
                "id": 200736354,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 200735326,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Audi_A4_allroad",
            "name": "A4 allroad",
            "niceName": "a4-allroad",
            "years": [{
                "id": 401665341,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW"]
        }, {
            "id": "Audi_A5",
            "name": "A5",
            "niceName": "a5",
            "years": [{
                "id": 200705417,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 200735833,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "FUTURE", "USED"]
        }, {
            "id": "Audi_A6",
            "name": "A6",
            "niceName": "a6",
            "years": [{
                "id": 200721615,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401644400,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Audi_A7",
            "name": "A7",
            "niceName": "a7",
            "years": [{
                "id": 200721614,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401644715,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Audi_A8",
            "name": "A8",
            "niceName": "a8",
            "years": [{
                "id": 200737487,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401645206,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "FUTURE", "USED"]
        }, {
            "id": "Audi_Q3",
            "name": "Q3",
            "niceName": "q3",
            "years": [{
                "id": 200736341,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401645530,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Audi_Q5",
            "name": "Q5",
            "niceName": "q5",
            "years": [{
                "id": 200737090,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401645902,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Audi_Q7",
            "name": "Q7",
            "niceName": "q7",
            "years": [{
                "id": 200736890,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Audi_R8",
            "name": "R8",
            "niceName": "r8",
            "years": [{
                "id": 401627093,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Audi_RS_7",
            "name": "RS 7",
            "niceName": "rs-7",
            "years": [{
                "id": 200725942,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401644717,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Audi_S3",
            "name": "S3",
            "niceName": "s3",
            "years": [{
                "id": 200736280,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401662199,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Audi_S4",
            "name": "S4",
            "niceName": "s4",
            "years": [{
                "id": 200736443,
                "year": 2016,
                "states": ["NEW", "USED"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Audi_S5",
            "name": "S5",
            "niceName": "s5",
            "years": [{
                "id": 200736807,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401644148,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "FUTURE", "USED"]
        }, {
            "id": "Audi_S6",
            "name": "S6",
            "niceName": "s6",
            "years": [{
                "id": 200725763,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401644401,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Audi_S7",
            "name": "S7",
            "niceName": "s7",
            "years": [{
                "id": 200725872,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401644716,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Audi_S8",
            "name": "S8",
            "niceName": "s8",
            "years": [{
                "id": 200737583,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401645213,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Audi_SQ5",
            "name": "SQ5",
            "niceName": "sq5",
            "years": [{
                "id": 200737091,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401645903,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Audi_TT",
            "name": "TT",
            "niceName": "tt",
            "years": [{
                "id": 200690719,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401646435,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Audi_TTS",
            "name": "TTS",
            "niceName": "tts",
            "years": [{
                "id": 200737739,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401646436,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Audi_allroad",
            "name": "allroad",
            "niceName": "allroad",
            "years": [{
                "id": 200736555,
                "year": 2016,
                "states": ["NEW", "USED"]
            }],
            "states": ["NEW", "USED"]
        }]
    }, {
        "id": 200000081,
        "name": "BMW",
        "niceName": "bmw",
        "models": [{
            "id": "BMW_2_Series",
            "name": "2 Series",
            "niceName": "2-series",
            "years": [{
                "id": 200744427,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401676566,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "BMW_3_Series",
            "name": "3 Series",
            "niceName": "3-series",
            "years": [{
                "id": 200729831,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401661575,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "BMW_3_Series_Gran_Turismo",
            "name": "3 Series Gran Turismo",
            "niceName": "3-series-gran-turismo",
            "years": [{
                "id": 200747547,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401672358,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "BMW_3_Series_eDrive",
            "name": "3 Series eDrive",
            "niceName": "3-series-edrive",
            "years": [{
                "id": 401638448,
                "year": 2016,
                "states": ["NEW", "USED"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "BMW_4_Series",
            "name": "4 Series",
            "niceName": "4-series",
            "years": [{
                "id": 200743641,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401671914,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "BMW_4_Series_Gran_Coupe",
            "name": "4 Series Gran Coupe",
            "niceName": "4-series-gran-coupe",
            "years": [{
                "id": 200737897,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401690406,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "BMW_5_Series",
            "name": "5 Series",
            "niceName": "5-series",
            "years": [{
                "id": 200745714,
                "year": 2016,
                "states": ["NEW", "USED"]
            }],
            "states": ["NEW", "FUTURE", "USED"]
        }, {
            "id": "BMW_5_Series_Gran_Turismo",
            "name": "5 Series Gran Turismo",
            "niceName": "5-series-gran-turismo",
            "years": [{
                "id": 200744768,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401667006,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "BMW_6_Series",
            "name": "6 Series",
            "niceName": "6-series",
            "years": [{
                "id": 200732865,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401642198,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "BMW_6_Series_Gran_Coupe",
            "name": "6 Series Gran Coupe",
            "niceName": "6-series-gran-coupe",
            "years": [{
                "id": 200734514,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401643859,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "BMW_7_Series",
            "name": "7 Series",
            "niceName": "7-series",
            "years": [{
                "id": 200737855,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401644387,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "BMW_ALPINA_B6_Gran_Coupe",
            "name": "ALPINA B6 Gran Coupe",
            "niceName": "alpina-b6-gran-coupe",
            "years": [{
                "id": 200735194,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401642313,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "BMW_ALPINA_B7",
            "name": "ALPINA B7",
            "niceName": "alpina-b7",
            "years": [{
                "id": 401690767,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "BMW_ActiveHybrid_5",
            "name": "ActiveHybrid 5",
            "niceName": "activehybrid-5",
            "years": [{
                "id": 401588568,
                "year": 2016,
                "states": ["NEW", "USED"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "BMW_M2",
            "name": "M2",
            "niceName": "m2",
            "years": [{
                "id": 401632199,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401660424,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "BMW_M3",
            "name": "M3",
            "niceName": "m3",
            "years": [{
                "id": 401566520,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401660142,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "BMW_M4",
            "name": "M4",
            "niceName": "m4",
            "years": [{
                "id": 200748861,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401660360,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "BMW_M4_GTS",
            "name": "M4 GTS",
            "niceName": "m4-gts",
            "years": [{
                "id": 401650415,
                "year": 2016,
                "states": ["NEW", "USED"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "BMW_M5",
            "name": "M5",
            "niceName": "m5",
            "years": [{
                "id": 200749889,
                "year": 2016,
                "states": ["NEW", "USED"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "BMW_M6",
            "name": "M6",
            "niceName": "m6",
            "years": [{
                "id": 200731110,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401643517,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "BMW_M6_Gran_Coupe",
            "name": "M6 Gran Coupe",
            "niceName": "m6-gran-coupe",
            "years": [{
                "id": 200731327,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401660037,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "BMW_X1",
            "name": "X1",
            "niceName": "x1",
            "years": [{
                "id": 200737084,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401658754,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "BMW_X3",
            "name": "X3",
            "niceName": "x3",
            "years": [{
                "id": 200734017,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401642716,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "BMW_X4",
            "name": "X4",
            "niceName": "x4",
            "years": [{
                "id": 200733790,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401642952,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "BMW_X5",
            "name": "X5",
            "niceName": "x5",
            "years": [{
                "id": 200730051,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401667507,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "BMW_X5_M",
            "name": "X5 M",
            "niceName": "x5-m",
            "years": [{
                "id": 401589056,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401667793,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "BMW_X5_eDrive",
            "name": "X5 eDrive",
            "niceName": "x5-edrive",
            "years": [{
                "id": 401583389,
                "year": 2016,
                "states": ["NEW", "USED"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "BMW_X6",
            "name": "X6",
            "niceName": "x6",
            "years": [{
                "id": 200761624,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401671407,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "BMW_X6_M",
            "name": "X6 M",
            "niceName": "x6-m",
            "years": [{
                "id": 200777975,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401671408,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "BMW_Z4",
            "name": "Z4",
            "niceName": "z4",
            "years": [{
                "id": 200733831,
                "year": 2016,
                "states": ["NEW", "USED"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "BMW_i3",
            "name": "i3",
            "niceName": "i3",
            "years": [{
                "id": 401612494,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401690178,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "BMW_i8",
            "name": "i8",
            "niceName": "i8",
            "years": [{
                "id": 401613126,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401677064,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }]
    }, {
        "id": 200005848,
        "name": "Bentley",
        "niceName": "bentley",
        "models": [{
            "id": "Bentley_Continental_GT",
            "name": "Continental GT",
            "niceName": "continental-gt",
            "years": [{
                "id": 401648526,
                "year": 2016,
                "states": ["NEW", "USED"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Bentley_Flying_Spur",
            "name": "Flying Spur",
            "niceName": "flying-spur",
            "years": [{
                "id": 401649583,
                "year": 2016,
                "states": ["NEW", "USED"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Bentley_Mulsanne",
            "name": "Mulsanne",
            "niceName": "mulsanne",
            "years": [{
                "id": 401646749,
                "year": 2016,
                "states": ["NEW", "USED"]
            }],
            "states": ["NEW", "USED"]
        }]
    }, {
        "id": 200006659,
        "name": "Buick",
        "niceName": "buick",
        "models": [{
            "id": "Buick_Cascada",
            "name": "Cascada",
            "niceName": "cascada",
            "years": [{
                "id": 200724880,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401671987,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Buick_Enclave",
            "name": "Enclave",
            "niceName": "enclave",
            "years": [{
                "id": 200740589,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 200732908,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Buick_Encore",
            "name": "Encore",
            "niceName": "encore",
            "years": [{
                "id": 401583524,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401631197,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Buick_Envision",
            "name": "Envision",
            "niceName": "envision",
            "years": [{
                "id": 200719677,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401640692,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Buick_LaCrosse",
            "name": "LaCrosse",
            "niceName": "lacrosse",
            "years": [{
                "id": 200746717,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401630402,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Buick_Regal",
            "name": "Regal",
            "niceName": "regal",
            "years": [{
                "id": 200751751,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401655334,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "FUTURE", "USED"]
        }, {
            "id": "Buick_Verano",
            "name": "Verano",
            "niceName": "verano",
            "years": [{
                "id": 200747588,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401659366,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }]
    }, {
        "id": 200001663,
        "name": "Cadillac",
        "niceName": "cadillac",
        "models": [{
            "id": "Cadillac_ATS",
            "name": "ATS",
            "niceName": "ats",
            "years": [{
                "id": 401580731,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401648800,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Cadillac_ATS_Coupe",
            "name": "ATS Coupe",
            "niceName": "ats-coupe",
            "years": [{
                "id": 401580732,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401650377,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Cadillac_ATS_V",
            "name": "ATS-V",
            "niceName": "ats-v",
            "years": [{
                "id": 200721610,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401655122,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Cadillac_CT6",
            "name": "CT6",
            "niceName": "ct6",
            "years": [{
                "id": 200693497,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401656078,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Cadillac_CTS",
            "name": "CTS",
            "niceName": "cts",
            "years": [{
                "id": 401578039,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401656286,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Cadillac_CTS_V",
            "name": "CTS-V",
            "niceName": "cts-v",
            "years": [{
                "id": 200688939,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401656704,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Cadillac_CTS_V_Coupe",
            "name": "CTS-V Coupe",
            "niceName": "cts-v-coupe",
            "years": [{
                "id": 200698421,
                "year": 2015,
                "states": ["NEW", "USED"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Cadillac_ELR",
            "name": "ELR",
            "niceName": "elr",
            "years": [{
                "id": 200714821,
                "year": 2016,
                "states": ["NEW", "USED"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Cadillac_Escalade",
            "name": "Escalade",
            "niceName": "escalade",
            "years": [{
                "id": 401575635,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401661753,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Cadillac_Escalade_ESV",
            "name": "Escalade ESV",
            "niceName": "escalade-esv",
            "years": [{
                "id": 401575637,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401661754,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Cadillac_SRX",
            "name": "SRX",
            "niceName": "srx",
            "years": [{
                "id": 200743965,
                "year": 2016,
                "states": ["NEW", "USED"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Cadillac_XT5",
            "name": "XT5",
            "niceName": "xt5",
            "years": [{
                "id": 200742448,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW"]
        }, {
            "id": "Cadillac_XTS",
            "name": "XTS",
            "niceName": "xts",
            "years": [{
                "id": 401566625,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401648451,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }]
    }, {
        "id": 200000404,
        "name": "Chevrolet",
        "niceName": "chevrolet",
        "models": [{
            "id": "Chevrolet_Bolt_EV",
            "name": "Bolt EV",
            "niceName": "bolt-ev",
            "years": [{
                "id": 200747011,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "FUTURE"]
        }, {
            "id": "Chevrolet_Camaro",
            "name": "Camaro",
            "niceName": "camaro",
            "years": [{
                "id": 200692011,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401642255,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Chevrolet_City_Express",
            "name": "City Express",
            "niceName": "city-express",
            "years": [{
                "id": 401631650,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401656851,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Chevrolet_Colorado",
            "name": "Colorado",
            "niceName": "colorado",
            "years": [{
                "id": 401575464,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401694981,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Chevrolet_Corvette",
            "name": "Corvette",
            "niceName": "corvette",
            "years": [{
                "id": 200744620,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401646226,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Chevrolet_Cruze",
            "name": "Cruze",
            "niceName": "cruze",
            "years": [{
                "id": 200492971,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401640813,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Chevrolet_Cruze_Limited",
            "name": "Cruze Limited",
            "niceName": "cruze-limited",
            "years": [{
                "id": 200745924,
                "year": 2016,
                "states": ["NEW", "USED"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Chevrolet_Equinox",
            "name": "Equinox",
            "niceName": "equinox",
            "years": [{
                "id": 200724433,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 200767372,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Chevrolet_Express",
            "name": "Express",
            "niceName": "express",
            "years": [{
                "id": 401626094,
                "year": 2016,
                "states": ["NEW", "USED"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Chevrolet_Express_Cargo",
            "name": "Express Cargo",
            "niceName": "express-cargo",
            "years": [{
                "id": 401630644,
                "year": 2016,
                "states": ["NEW", "USED"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Chevrolet_Impala",
            "name": "Impala",
            "niceName": "impala",
            "years": [{
                "id": 200779605,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401642197,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Chevrolet_Malibu",
            "name": "Malibu",
            "niceName": "malibu",
            "years": [{
                "id": 200731215,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401657957,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Chevrolet_Malibu_Limited",
            "name": "Malibu Limited",
            "niceName": "malibu-limited",
            "years": [{
                "id": 200747325,
                "year": 2016,
                "states": ["NEW", "USED"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Chevrolet_SS",
            "name": "SS",
            "niceName": "ss",
            "years": [{
                "id": 401614830,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401695999,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Chevrolet_Silverado_1500",
            "name": "Silverado 1500",
            "niceName": "silverado-1500",
            "years": [{
                "id": 200746487,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 200731902,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Chevrolet_Silverado_2500HD",
            "name": "Silverado 2500HD",
            "niceName": "silverado-2500hd",
            "years": [{
                "id": 401597676,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401611387,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "FUTURE", "USED"]
        }, {
            "id": "Chevrolet_Silverado_3500HD",
            "name": "Silverado 3500HD",
            "niceName": "silverado-3500hd",
            "years": [{
                "id": 401612110,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401611388,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "FUTURE", "USED"]
        }, {
            "id": "Chevrolet_Sonic",
            "name": "Sonic",
            "niceName": "sonic",
            "years": [{
                "id": 401566568,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401655480,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Chevrolet_Spark",
            "name": "Spark",
            "niceName": "spark",
            "years": [{
                "id": 200731216,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401642030,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Chevrolet_Spark_EV",
            "name": "Spark EV",
            "niceName": "spark-ev",
            "years": [{
                "id": 401625835,
                "year": 2016,
                "states": ["NEW", "USED"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Chevrolet_Suburban",
            "name": "Suburban",
            "niceName": "suburban",
            "years": [{
                "id": 200749036,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401659726,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Chevrolet_Tahoe",
            "name": "Tahoe",
            "niceName": "tahoe",
            "years": [{
                "id": 200749035,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401658457,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Chevrolet_Traverse",
            "name": "Traverse",
            "niceName": "traverse",
            "years": [{
                "id": 200738878,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 200732904,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Chevrolet_Trax",
            "name": "Trax",
            "niceName": "trax",
            "years": [{
                "id": 200779606,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401660185,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Chevrolet_Volt",
            "name": "Volt",
            "niceName": "volt",
            "years": [{
                "id": 200707596,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401626580,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }]
    }, {
        "id": 200003644,
        "name": "Chrysler",
        "niceName": "chrysler",
        "models": [{
            "id": "Chrysler_200",
            "name": "200",
            "niceName": "200",
            "years": [{
                "id": 200741377,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401649771,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Chrysler_300",
            "name": "300",
            "niceName": "300",
            "years": [{
                "id": 200751747,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401676925,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Chrysler_Pacifica",
            "name": "Pacifica",
            "niceName": "pacifica",
            "years": [{
                "id": 200728424,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Chrysler_Pacifica_Hybrid",
            "name": "Pacifica Hybrid",
            "niceName": "pacifica-hybrid",
            "years": [{
                "id": 401695771,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW"]
        }, {
            "id": "Chrysler_Town_and_Country",
            "name": "Town and Country",
            "niceName": "town-and-country",
            "years": [{
                "id": 200696428,
                "year": 2016,
                "states": ["NEW", "USED"]
            }],
            "states": ["NEW", "USED"]
        }]
    }, {
        "id": 200009788,
        "name": "Dodge",
        "niceName": "dodge",
        "models": [{
            "id": "Dodge_Challenger",
            "name": "Challenger",
            "niceName": "challenger",
            "years": [{
                "id": 200782175,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401676479,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Dodge_Charger",
            "name": "Charger",
            "niceName": "charger",
            "years": [{
                "id": 200751340,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401671902,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Dodge_Dart",
            "name": "Dart",
            "niceName": "dart",
            "years": [{
                "id": 200738444,
                "year": 2016,
                "states": ["NEW", "USED"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Dodge_Durango",
            "name": "Durango",
            "niceName": "durango",
            "years": [{
                "id": 401598014,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401647934,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Dodge_Grand_Caravan",
            "name": "Grand Caravan",
            "niceName": "grand-caravan",
            "years": [{
                "id": 200741043,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401647873,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Dodge_Journey",
            "name": "Journey",
            "niceName": "journey",
            "years": [{
                "id": 200741339,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401654841,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Dodge_Viper",
            "name": "Viper",
            "niceName": "viper",
            "years": [{
                "id": 200734566,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401649364,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }]
    }, {
        "id": 200033022,
        "name": "FIAT",
        "niceName": "fiat",
        "models": [{
            "id": "FIAT_124_Spider",
            "name": "124 Spider",
            "niceName": "124-spider",
            "years": [{
                "id": 200742453,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW"]
        }, {
            "id": "FIAT_500",
            "name": "500",
            "niceName": "500",
            "years": [{
                "id": 401572290,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401654792,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "FIAT_500L",
            "name": "500L",
            "niceName": "500l",
            "years": [{
                "id": 401573921,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401660159,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "FIAT_500X",
            "name": "500X",
            "niceName": "500x",
            "years": [{
                "id": 200721405,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401665073,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "FIAT_500e",
            "name": "500e",
            "niceName": "500e",
            "years": [{
                "id": 401566592,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401655398,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }]
    }, {
        "id": 200006023,
        "name": "Ferrari",
        "niceName": "ferrari",
        "models": [{
            "id": "Ferrari_458_Italia",
            "name": "458 Italia",
            "niceName": "458-italia",
            "years": [{
                "id": 200725112,
                "year": 2015,
                "states": ["NEW", "USED"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Ferrari_California_T",
            "name": "California T",
            "niceName": "california-t",
            "years": [{
                "id": 200725168,
                "year": 2015,
                "states": ["NEW", "USED"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Ferrari_F12_Berlinetta",
            "name": "F12 Berlinetta",
            "niceName": "f12-berlinetta",
            "years": [{
                "id": 200725113,
                "year": 2015,
                "states": ["NEW", "USED"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Ferrari_FF",
            "name": "FF",
            "niceName": "ff",
            "years": [{
                "id": 200725114,
                "year": 2015,
                "states": ["NEW", "USED"]
            }],
            "states": ["NEW", "USED"]
        }]
    }, {
        "id": 200005143,
        "name": "Ford",
        "niceName": "ford",
        "models": [{
            "id": "Ford_C_Max_Energi",
            "name": "C-Max Energi",
            "niceName": "c-max-energi",
            "years": [{
                "id": 200741402,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401671899,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Ford_C_Max_Hybrid",
            "name": "C-Max Hybrid",
            "niceName": "c-max-hybrid",
            "years": [{
                "id": 200742267,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401672228,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Ford_Edge",
            "name": "Edge",
            "niceName": "edge",
            "years": [{
                "id": 401589394,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401670676,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Ford_Escape",
            "name": "Escape",
            "niceName": "escape",
            "years": [{
                "id": 200733433,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 200735321,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Ford_Expedition",
            "name": "Expedition",
            "niceName": "expedition",
            "years": [{
                "id": 200734913,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401639337,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "FUTURE", "USED"]
        }, {
            "id": "Ford_Explorer",
            "name": "Explorer",
            "niceName": "explorer",
            "years": [{
                "id": 200693542,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401638388,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Ford_F_150",
            "name": "F-150",
            "niceName": "f-150",
            "years": [{
                "id": 401582329,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 200724856,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Ford_F_250_Super_Duty",
            "name": "F-250 Super Duty",
            "niceName": "f-250-super-duty",
            "years": [{
                "id": 200730134,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 200729834,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Ford_F_350_Super_Duty",
            "name": "F-350 Super Duty",
            "niceName": "f-350-super-duty",
            "years": [{
                "id": 200730256,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401611393,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Ford_F_450_Super_Duty",
            "name": "F-450 Super Duty",
            "niceName": "f-450-super-duty",
            "years": [{
                "id": 200730703,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401641440,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Ford_Fiesta",
            "name": "Fiesta",
            "niceName": "fiesta",
            "years": [{
                "id": 200733229,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401677703,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Ford_Flex",
            "name": "Flex",
            "niceName": "flex",
            "years": [{
                "id": 401593852,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401676499,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Ford_Focus",
            "name": "Focus",
            "niceName": "focus",
            "years": [{
                "id": 200740244,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401670491,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Ford_Focus_RS",
            "name": "Focus RS",
            "niceName": "focus-rs",
            "years": [{
                "id": 401590246,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401657504,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Ford_Focus_ST",
            "name": "Focus ST",
            "niceName": "focus-st",
            "years": [{
                "id": 200740480,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401671802,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Ford_Fusion",
            "name": "Fusion",
            "niceName": "fusion",
            "years": [{
                "id": 200727079,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 200732915,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Ford_Fusion_Energi",
            "name": "Fusion Energi",
            "niceName": "fusion-energi",
            "years": [{
                "id": 200728167,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401630049,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Ford_Fusion_Hybrid",
            "name": "Fusion Hybrid",
            "niceName": "fusion-hybrid",
            "years": [{
                "id": 200727948,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401629469,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Ford_Mustang",
            "name": "Mustang",
            "niceName": "mustang",
            "years": [{
                "id": 200734939,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401640292,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Ford_Shelby_GT350",
            "name": "Shelby GT350",
            "niceName": "shelby-gt350",
            "years": [{
                "id": 200736080,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401640216,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Ford_Taurus",
            "name": "Taurus",
            "niceName": "taurus",
            "years": [{
                "id": 200700837,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401672275,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Ford_Transit_Connect",
            "name": "Transit Connect",
            "niceName": "transit-connect",
            "years": [{
                "id": 200732435,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401640459,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Ford_Transit_Van",
            "name": "Transit Van",
            "niceName": "transit-van",
            "years": [{
                "id": 200735424,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401643850,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Ford_Transit_Wagon",
            "name": "Transit Wagon",
            "niceName": "transit-wagon",
            "years": [{
                "id": 200735346,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401646996,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }]
    }, {
        "id": 200007302,
        "name": "GMC",
        "niceName": "gmc",
        "models": [{
            "id": "GMC_Acadia",
            "name": "Acadia",
            "niceName": "acadia",
            "years": [{
                "id": 200741268,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 200732912,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "GMC_Acadia_Limited",
            "name": "Acadia Limited",
            "niceName": "acadia-limited",
            "years": [{
                "id": 401656954,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW"]
        }, {
            "id": "GMC_Canyon",
            "name": "Canyon",
            "niceName": "canyon",
            "years": [{
                "id": 401575440,
                "year": 2016,
                "states": ["NEW", "USED"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "GMC_Savana",
            "name": "Savana",
            "niceName": "savana",
            "years": [{
                "id": 401625993,
                "year": 2016,
                "states": ["NEW", "USED"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "GMC_Savana_Cargo",
            "name": "Savana Cargo",
            "niceName": "savana-cargo",
            "years": [{
                "id": 401626232,
                "year": 2016,
                "states": ["NEW", "USED"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "GMC_Sierra_1500",
            "name": "Sierra 1500",
            "niceName": "sierra-1500",
            "years": [{
                "id": 401589563,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 200732918,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "FUTURE", "USED"]
        }, {
            "id": "GMC_Sierra_2500HD",
            "name": "Sierra 2500HD",
            "niceName": "sierra-2500hd",
            "years": [{
                "id": 401630179,
                "year": 2016,
                "states": ["NEW", "USED"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "GMC_Sierra_3500HD",
            "name": "Sierra 3500HD",
            "niceName": "sierra-3500hd",
            "years": [{
                "id": 401613795,
                "year": 2016,
                "states": ["NEW", "USED"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "GMC_Terrain",
            "name": "Terrain",
            "niceName": "terrain",
            "years": [{
                "id": 200746361,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401645483,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "GMC_Yukon",
            "name": "Yukon",
            "niceName": "yukon",
            "years": [{
                "id": 200779855,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401660835,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "GMC_Yukon_XL",
            "name": "Yukon XL",
            "niceName": "yukon-xl",
            "years": [{
                "id": 200779856,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401660836,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }]
    }, {
        "id": 401626455,
        "name": "Genesis",
        "niceName": "genesis",
        "models": [{
            "id": "Genesis_G80",
            "name": "G80",
            "niceName": "g80",
            "years": [{
                "id": 401597817,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW"]
        }, {
            "id": "Genesis_G90",
            "name": "G90",
            "niceName": "g90",
            "years": [{
                "id": 401597818,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "FUTURE"]
        }]
    }, {
        "id": 200001444,
        "name": "Honda",
        "niceName": "honda",
        "models": [{
            "id": "Honda_Accord",
            "name": "Accord",
            "niceName": "accord",
            "years": [{
                "id": 200751251,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401649920,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Honda_Accord_Hybrid",
            "name": "Accord Hybrid",
            "niceName": "accord-hybrid",
            "years": [{
                "id": 200709439,
                "year": 2015,
                "states": ["NEW", "USED"]
            }, {
                "id": 401644272,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Honda_CR_V",
            "name": "CR-V",
            "niceName": "cr-v",
            "years": [{
                "id": 401582803,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401696111,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Honda_CR_Z",
            "name": "CR-Z",
            "niceName": "cr-z",
            "years": [{
                "id": 401613419,
                "year": 2016,
                "states": ["NEW", "USED"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Honda_Civic",
            "name": "Civic",
            "niceName": "civic",
            "years": [{
                "id": 200731211,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401660820,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Honda_Crosstour",
            "name": "Crosstour",
            "niceName": "crosstour",
            "years": [{
                "id": 200712325,
                "year": 2015,
                "states": ["NEW", "USED"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Honda_Fit",
            "name": "Fit",
            "niceName": "fit",
            "years": [{
                "id": 200742363,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401666660,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Honda_HR_V",
            "name": "HR-V",
            "niceName": "hr-v",
            "years": [{
                "id": 200723508,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401672334,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Honda_Odyssey",
            "name": "Odyssey",
            "niceName": "odyssey",
            "years": [{
                "id": 200751250,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401633972,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "FUTURE", "USED"]
        }, {
            "id": "Honda_Pilot",
            "name": "Pilot",
            "niceName": "pilot",
            "years": [{
                "id": 200707980,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401691087,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Honda_Ridgeline",
            "name": "Ridgeline",
            "niceName": "ridgeline",
            "years": [{
                "id": 401625742,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }]
    }, {
        "id": 200001398,
        "name": "Hyundai",
        "niceName": "hyundai",
        "models": [{
            "id": "Hyundai_Accent",
            "name": "Accent",
            "niceName": "accent",
            "years": [{
                "id": 200759750,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401694794,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Hyundai_Azera",
            "name": "Azera",
            "niceName": "azera",
            "years": [{
                "id": 401590268,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401690787,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Hyundai_Elantra",
            "name": "Elantra",
            "niceName": "elantra",
            "years": [{
                "id": 200711257,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401627592,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Hyundai_Elantra_GT",
            "name": "Elantra GT",
            "niceName": "elantra-gt",
            "years": [{
                "id": 200728304,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401667436,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Hyundai_Equus",
            "name": "Equus",
            "niceName": "equus",
            "years": [{
                "id": 200738131,
                "year": 2016,
                "states": ["NEW", "USED"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Hyundai_Genesis",
            "name": "Genesis",
            "niceName": "genesis",
            "years": [{
                "id": 401593919,
                "year": 2016,
                "states": ["NEW", "USED"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Hyundai_Genesis_Coupe",
            "name": "Genesis Coupe",
            "niceName": "genesis-coupe",
            "years": [{
                "id": 401597974,
                "year": 2016,
                "states": ["NEW", "USED"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Hyundai_Santa_Fe",
            "name": "Santa Fe",
            "niceName": "santa-fe",
            "years": [{
                "id": 200744830,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401628704,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Hyundai_Santa_Fe_Sport",
            "name": "Santa Fe Sport",
            "niceName": "santa-fe-sport",
            "years": [{
                "id": 200736734,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401627422,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Hyundai_Sonata",
            "name": "Sonata",
            "niceName": "sonata",
            "years": [{
                "id": 401575488,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401655737,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Hyundai_Sonata_Hybrid",
            "name": "Sonata Hybrid",
            "niceName": "sonata-hybrid",
            "years": [{
                "id": 200741595,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401676302,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Hyundai_Sonata_Plug_in_Hybrid",
            "name": "Sonata Plug-in Hybrid",
            "niceName": "sonata-plug-in-hybrid",
            "years": [{
                "id": 401597449,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401672397,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Hyundai_Tucson",
            "name": "Tucson",
            "niceName": "tucson",
            "years": [{
                "id": 200706999,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401659779,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Hyundai_Veloster",
            "name": "Veloster",
            "niceName": "veloster",
            "years": [{
                "id": 200749829,
                "year": 2016,
                "states": ["NEW", "USED"]
            }],
            "states": ["NEW", "USED"]
        }]
    }, {
        "id": 200000089,
        "name": "Infiniti",
        "niceName": "infiniti",
        "models": [{
            "id": "Infiniti_Q50",
            "name": "Q50",
            "niceName": "q50",
            "years": [{
                "id": 401630272,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401678843,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Infiniti_Q60_Coupe",
            "name": "Q60 Coupe",
            "niceName": "q60-coupe",
            "years": [{
                "id": 200724867,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Infiniti_Q70",
            "name": "Q70",
            "niceName": "q70",
            "years": [{
                "id": 401613041,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401695704,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Infiniti_QX30",
            "name": "QX30",
            "niceName": "qx30",
            "years": [{
                "id": 200781954,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "FUTURE"]
        }, {
            "id": "Infiniti_QX50",
            "name": "QX50",
            "niceName": "qx50",
            "years": [{
                "id": 401574226,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401671430,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Infiniti_QX60",
            "name": "QX60",
            "niceName": "qx60",
            "years": [{
                "id": 401630503,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401690293,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Infiniti_QX70",
            "name": "QX70",
            "niceName": "qx70",
            "years": [{
                "id": 200736081,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401661090,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Infiniti_QX80",
            "name": "QX80",
            "niceName": "qx80",
            "years": [{
                "id": 401610857,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401694333,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }]
    }, {
        "id": 200003196,
        "name": "Jaguar",
        "niceName": "jaguar",
        "models": [{
            "id": "Jaguar_F_PACE",
            "name": "F-PACE",
            "niceName": "f-pace",
            "years": [{
                "id": 200722245,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW"]
        }, {
            "id": "Jaguar_F_TYPE",
            "name": "F-TYPE",
            "niceName": "f-type",
            "years": [{
                "id": 200721393,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401631556,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Jaguar_XE",
            "name": "XE",
            "niceName": "xe",
            "years": [{
                "id": 200716564,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW"]
        }, {
            "id": "Jaguar_XF",
            "name": "XF",
            "niceName": "xf",
            "years": [{
                "id": 200730062,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401630426,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Jaguar_XJ",
            "name": "XJ",
            "niceName": "xj",
            "years": [{
                "id": 401583347,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401679090,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }]
    }, {
        "id": 200001510,
        "name": "Jeep",
        "niceName": "jeep",
        "models": [{
            "id": "Jeep_Cherokee",
            "name": "Cherokee",
            "niceName": "cherokee",
            "years": [{
                "id": 200735583,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401648052,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Jeep_Compass",
            "name": "Compass",
            "niceName": "compass",
            "years": [{
                "id": 200738833,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401647282,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Jeep_Grand_Cherokee",
            "name": "Grand Cherokee",
            "niceName": "grand-cherokee",
            "years": [{
                "id": 401589152,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401647932,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Jeep_Grand_Cherokee_SRT",
            "name": "Grand Cherokee SRT",
            "niceName": "grand-cherokee-srt",
            "years": [{
                "id": 401598494,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401657873,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Jeep_Patriot",
            "name": "Patriot",
            "niceName": "patriot",
            "years": [{
                "id": 200737268,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401647283,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Jeep_Renegade",
            "name": "Renegade",
            "niceName": "renegade",
            "years": [{
                "id": 401566694,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401662360,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Jeep_Wrangler",
            "name": "Wrangler",
            "niceName": "wrangler",
            "years": [{
                "id": 200747759,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401661440,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "FUTURE", "USED"]
        }]
    }, {
        "id": 200003063,
        "name": "Kia",
        "niceName": "kia",
        "models": [{
            "id": "Kia_Cadenza",
            "name": "Cadenza",
            "niceName": "cadenza",
            "years": [{
                "id": 401583132,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401610776,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "FUTURE", "USED"]
        }, {
            "id": "Kia_Forte",
            "name": "Forte",
            "niceName": "forte",
            "years": [{
                "id": 200745336,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401637969,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Kia_K900",
            "name": "K900",
            "niceName": "k900",
            "years": [{
                "id": 401612184,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401695448,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Kia_Optima",
            "name": "Optima",
            "niceName": "optima",
            "years": [{
                "id": 200710532,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401696013,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Kia_Optima_Hybrid",
            "name": "Optima Hybrid",
            "niceName": "optima-hybrid",
            "years": [{
                "id": 401597525,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401691193,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Kia_Rio",
            "name": "Rio",
            "niceName": "rio",
            "years": [{
                "id": 200739903,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401670902,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Kia_Sedona",
            "name": "Sedona",
            "niceName": "sedona",
            "years": [{
                "id": 200743579,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401678313,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Kia_Sorento",
            "name": "Sorento",
            "niceName": "sorento",
            "years": [{
                "id": 200707602,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401643123,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Kia_Soul",
            "name": "Soul",
            "niceName": "soul",
            "years": [{
                "id": 200748658,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401693669,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Kia_Soul_EV",
            "name": "Soul EV",
            "niceName": "soul-ev",
            "years": [{
                "id": 200746122,
                "year": 2016,
                "states": ["NEW", "USED"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Kia_Sportage",
            "name": "Sportage",
            "niceName": "sportage",
            "years": [{
                "id": 200743048,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401578389,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }]
    }, {
        "id": 200005922,
        "name": "Lamborghini",
        "niceName": "lamborghini",
        "models": [{
            "id": "Lamborghini_Aventador",
            "name": "Aventador",
            "niceName": "aventador",
            "years": [{
                "id": 401638360,
                "year": 2016,
                "states": ["NEW", "USED"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Lamborghini_Huracan",
            "name": "Huracan",
            "niceName": "huracan",
            "years": [{
                "id": 401637964,
                "year": 2016,
                "states": ["NEW", "USED"]
            }],
            "states": ["NEW", "USED"]
        }]
    }, {
        "id": 200006582,
        "name": "Land Rover",
        "niceName": "land-rover",
        "models": [{
            "id": "Land_Rover_Discovery_Sport",
            "name": "Discovery Sport",
            "niceName": "discovery-sport",
            "years": [{
                "id": 401575208,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401671619,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Land_Rover_LR4",
            "name": "LR4",
            "niceName": "lr4",
            "years": [{
                "id": 401575011,
                "year": 2016,
                "states": ["NEW", "USED"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Land_Rover_Range_Rover",
            "name": "Range Rover",
            "niceName": "range-rover",
            "years": [{
                "id": 200724860,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401700107,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Land_Rover_Range_Rover_Evoque",
            "name": "Range Rover Evoque",
            "niceName": "range-rover-evoque",
            "years": [{
                "id": 200733989,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 200730058,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Land_Rover_Range_Rover_Sport",
            "name": "Range Rover Sport",
            "niceName": "range-rover-sport",
            "years": [{
                "id": 200724861,
                "year": 2016,
                "states": ["NEW", "USED"]
            }],
            "states": ["NEW", "USED"]
        }]
    }, {
        "id": 200001623,
        "name": "Lexus",
        "niceName": "lexus",
        "models": [{
            "id": "Lexus_CT_200h",
            "name": "CT 200h",
            "niceName": "ct-200h",
            "years": [{
                "id": 200747263,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401657466,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Lexus_ES_300h",
            "name": "ES 300h",
            "niceName": "es-300h",
            "years": [{
                "id": 200746206,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401659437,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Lexus_ES_350",
            "name": "ES 350",
            "niceName": "es-350",
            "years": [{
                "id": 200745233,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401659438,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Lexus_GS_200t",
            "name": "GS 200t",
            "niceName": "gs-200t",
            "years": [{
                "id": 401611403,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401691156,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Lexus_GS_350",
            "name": "GS 350",
            "niceName": "gs-350",
            "years": [{
                "id": 401611547,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401678907,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Lexus_GS_450h",
            "name": "GS 450h",
            "niceName": "gs-450h",
            "years": [{
                "id": 401583471,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401692373,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Lexus_GS_F",
            "name": "GS F",
            "niceName": "gs-f",
            "years": [{
                "id": 200724405,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401661661,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Lexus_GX_460",
            "name": "GX 460",
            "niceName": "gx-460",
            "years": [{
                "id": 200747262,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401659439,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Lexus_IS_200t",
            "name": "IS 200t",
            "niceName": "is-200t",
            "years": [{
                "id": 200747202,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401690859,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Lexus_IS_300",
            "name": "IS 300",
            "niceName": "is-300",
            "years": [{
                "id": 200747203,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401690860,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Lexus_IS_350",
            "name": "IS 350",
            "niceName": "is-350",
            "years": [{
                "id": 200747204,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401690861,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Lexus_LS_460",
            "name": "LS 460",
            "niceName": "ls-460",
            "years": [{
                "id": 401580676,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401678992,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Lexus_LS_600h_L",
            "name": "LS 600h L",
            "niceName": "ls-600h-l",
            "years": [{
                "id": 401612857,
                "year": 2016,
                "states": ["NEW", "USED"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Lexus_LX_570",
            "name": "LX 570",
            "niceName": "lx-570",
            "years": [{
                "id": 401582735,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401659440,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Lexus_NX_200t",
            "name": "NX 200t",
            "niceName": "nx-200t",
            "years": [{
                "id": 401610907,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401661659,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Lexus_NX_300h",
            "name": "NX 300h",
            "niceName": "nx-300h",
            "years": [{
                "id": 401610908,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401661660,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Lexus_RC_200t",
            "name": "RC 200t",
            "niceName": "rc-200t",
            "years": [{
                "id": 401594007,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401689868,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Lexus_RC_300",
            "name": "RC 300",
            "niceName": "rc-300",
            "years": [{
                "id": 401594008,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401689905,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Lexus_RC_350",
            "name": "RC 350",
            "niceName": "rc-350",
            "years": [{
                "id": 401594009,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401689902,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Lexus_RC_F",
            "name": "RC F",
            "niceName": "rc-f",
            "years": [{
                "id": 401594010,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401689903,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Lexus_RX_350",
            "name": "RX 350",
            "niceName": "rx-350",
            "years": [{
                "id": 200730077,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401660462,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Lexus_RX_450h",
            "name": "RX 450h",
            "niceName": "rx-450h",
            "years": [{
                "id": 401589089,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401660463,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }]
    }, {
        "id": 200001777,
        "name": "Lincoln",
        "niceName": "lincoln",
        "models": [{
            "id": "Lincoln_Continental",
            "name": "Continental",
            "niceName": "continental",
            "years": [{
                "id": 200730686,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Lincoln_MKC",
            "name": "MKC",
            "niceName": "mkc",
            "years": [{
                "id": 200732076,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401630379,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Lincoln_MKS",
            "name": "MKS",
            "niceName": "mks",
            "years": [{
                "id": 401581230,
                "year": 2016,
                "states": ["NEW", "USED"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Lincoln_MKT",
            "name": "MKT",
            "niceName": "mkt",
            "years": [{
                "id": 401593848,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401670628,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Lincoln_MKX",
            "name": "MKX",
            "niceName": "mkx",
            "years": [{
                "id": 200696421,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401677052,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Lincoln_MKZ",
            "name": "MKZ",
            "niceName": "mkz",
            "years": [{
                "id": 200729075,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401630475,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Lincoln_Navigator",
            "name": "Navigator",
            "niceName": "navigator",
            "years": [{
                "id": 200737083,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401640543,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }]
    }, {
        "id": 200006242,
        "name": "Lotus",
        "niceName": "lotus",
        "models": [{
            "id": "Lotus_Evora_400",
            "name": "Evora 400",
            "niceName": "evora-400",
            "years": [{
                "id": 401666186,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW"]
        }]
    }, {
        "id": 200002305,
        "name": "MINI",
        "niceName": "mini",
        "models": [{
            "id": "MINI_Clubman",
            "name": "Clubman",
            "niceName": "clubman",
            "years": [{
                "id": 401656746,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW"]
        }, {
            "id": "MINI_Convertible",
            "name": "Convertible",
            "niceName": "convertible",
            "years": [{
                "id": 401655076,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW"]
        }, {
            "id": "MINI_Cooper",
            "name": "Cooper",
            "niceName": "cooper",
            "years": [{
                "id": 200738845,
                "year": 2016,
                "states": ["NEW", "USED"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "MINI_Cooper_Clubman",
            "name": "Cooper Clubman",
            "niceName": "cooper-clubman",
            "years": [{
                "id": 200741085,
                "year": 2016,
                "states": ["NEW", "USED"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "MINI_Cooper_Countryman",
            "name": "Cooper Countryman",
            "niceName": "cooper-countryman",
            "years": [{
                "id": 200736666,
                "year": 2016,
                "states": ["NEW", "USED"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "MINI_Cooper_Paceman",
            "name": "Cooper Paceman",
            "niceName": "cooper-paceman",
            "years": [{
                "id": 200745062,
                "year": 2016,
                "states": ["NEW", "USED"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "MINI_Hardtop_2_Door",
            "name": "Hardtop 2 Door",
            "niceName": "hardtop-2-door",
            "years": [{
                "id": 401658048,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW"]
        }, {
            "id": "MINI_Hardtop_4_Door",
            "name": "Hardtop 4 Door",
            "niceName": "hardtop-4-door",
            "years": [{
                "id": 401694183,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW"]
        }]
    }, {
        "id": 200028029,
        "name": "Maserati",
        "niceName": "maserati",
        "models": [{
            "id": "Maserati_Ghibli",
            "name": "Ghibli",
            "niceName": "ghibli",
            "years": [{
                "id": 401583224,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401661436,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Maserati_GranTurismo",
            "name": "GranTurismo",
            "niceName": "granturismo",
            "years": [{
                "id": 401588487,
                "year": 2016,
                "states": ["NEW", "USED"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Maserati_GranTurismo_Convertible",
            "name": "GranTurismo Convertible",
            "niceName": "granturismo-convertible",
            "years": [{
                "id": 401590484,
                "year": 2016,
                "states": ["NEW", "USED"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Maserati_Levante",
            "name": "Levante",
            "niceName": "levante",
            "years": [{
                "id": 401633528,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW"]
        }, {
            "id": "Maserati_Quattroporte",
            "name": "Quattroporte",
            "niceName": "quattroporte",
            "years": [{
                "id": 401597824,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401661437,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }]
    }, {
        "id": 200004100,
        "name": "Mazda",
        "niceName": "mazda",
        "models": [{
            "id": "Mazda_3",
            "name": "3",
            "niceName": "3",
            "years": [{
                "id": 200703374,
                "year": 2015,
                "states": ["NEW", "USED"]
            }, {
                "id": 200743726,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401676798,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Mazda_5",
            "name": "5",
            "niceName": "5",
            "years": [{
                "id": 200715548,
                "year": 2015,
                "states": ["NEW", "USED"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Mazda_6",
            "name": "6",
            "niceName": "6",
            "years": [{
                "id": 200673389,
                "year": 2015,
                "states": ["NEW", "USED"]
            }, {
                "id": 200724972,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401662075,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Mazda_CX_3",
            "name": "CX-3",
            "niceName": "cx-3",
            "years": [{
                "id": 200719665,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401658825,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Mazda_CX_5",
            "name": "CX-5",
            "niceName": "cx-5",
            "years": [{
                "id": 200673388,
                "year": 2015,
                "states": ["NEW", "USED"]
            }, {
                "id": 200726398,
                "year": 2016,
                "states": ["NEW", "USED"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Mazda_CX_9",
            "name": "CX-9",
            "niceName": "cx-9",
            "years": [{
                "id": 200710337,
                "year": 2015,
                "states": ["NEW", "USED"]
            }, {
                "id": 401626203,
                "year": 2016,
                "states": ["NEW", "USED"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Mazda_MX_5_Miata",
            "name": "MX-5 Miata",
            "niceName": "mx-5-miata",
            "years": [{
                "id": 200695187,
                "year": 2015,
                "states": ["NEW", "USED"]
            }, {
                "id": 200692013,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401695169,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Mazda_MX_5_Miata_RF",
            "name": "MX-5 Miata RF",
            "niceName": "mx-5-miata-rf",
            "years": [{
                "id": 401678573,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW"]
        }]
    }, {
        "id": 200051397,
        "name": "McLaren",
        "niceName": "mclaren",
        "models": [{
            "id": "McLaren_570GT",
            "name": "570GT",
            "niceName": "570gt",
            "years": [{
                "id": 401696101,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW"]
        }, {
            "id": "McLaren_570S",
            "name": "570S",
            "niceName": "570s",
            "years": [{
                "id": 401638463,
                "year": 2016,
                "states": ["NEW", "USED"]
            }],
            "states": ["NEW", "FUTURE", "USED"]
        }]
    }, {
        "id": 200000130,
        "name": "Mercedes-Benz",
        "niceName": "mercedes-benz",
        "models": [{
            "id": "Mercedes_Benz_AMG_GT",
            "name": "AMG GT",
            "niceName": "amg-gt",
            "years": [{
                "id": 200700831,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401665249,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Mercedes_Benz_B_Class_Electric_Drive",
            "name": "B-Class Electric Drive",
            "niceName": "b-class-electric-drive",
            "years": [{
                "id": 401598100,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401667829,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Mercedes_Benz_C_Class",
            "name": "C-Class",
            "niceName": "c-class",
            "years": [{
                "id": 200773057,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401578396,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Mercedes_Benz_CLA_Class",
            "name": "CLA-Class",
            "niceName": "cla-class",
            "years": [{
                "id": 401601386,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401665028,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Mercedes_Benz_CLS_Class",
            "name": "CLS-Class",
            "niceName": "cls-class",
            "years": [{
                "id": 200745885,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401670634,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Mercedes_Benz_E_Class",
            "name": "E-Class",
            "niceName": "e-class",
            "years": [{
                "id": 200732924,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401626400,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Mercedes_Benz_G_Class",
            "name": "G-Class",
            "niceName": "g-class",
            "years": [{
                "id": 401597152,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401646829,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "FUTURE", "USED"]
        }, {
            "id": "Mercedes_Benz_GL_Class",
            "name": "GL-Class",
            "niceName": "gl-class",
            "years": [{
                "id": 200732530,
                "year": 2016,
                "states": ["NEW", "USED"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Mercedes_Benz_GLA_Class",
            "name": "GLA-Class",
            "niceName": "gla-class",
            "years": [{
                "id": 401597610,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401660386,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Mercedes_Benz_GLC_Class",
            "name": "GLC-Class",
            "niceName": "glc-class",
            "years": [{
                "id": 200735398,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401638662,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Mercedes_Benz_GLC_Class_Coupe",
            "name": "GLC-Class Coupe",
            "niceName": "glc-class-coupe",
            "years": [{
                "id": 401638663,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "FUTURE"]
        }, {
            "id": "Mercedes_Benz_GLE_Class",
            "name": "GLE-Class",
            "niceName": "gle-class",
            "years": [{
                "id": 200694317,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401660730,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Mercedes_Benz_GLE_Class_Coupe",
            "name": "GLE-Class Coupe",
            "niceName": "gle-class-coupe",
            "years": [{
                "id": 200749645,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401661206,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Mercedes_Benz_GLS_Class",
            "name": "GLS-Class",
            "niceName": "gls-class",
            "years": [{
                "id": 401641435,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW"]
        }, {
            "id": "Mercedes_Benz_Maybach",
            "name": "Maybach",
            "niceName": "maybach",
            "years": [{
                "id": 200721611,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401670461,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Mercedes_Benz_Metris",
            "name": "Metris",
            "niceName": "metris",
            "years": [{
                "id": 200721408,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401699783,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Mercedes_Benz_S_Class",
            "name": "S-Class",
            "niceName": "s-class",
            "years": [{
                "id": 200713462,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401578397,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Mercedes_Benz_SL_Class",
            "name": "SL-Class",
            "niceName": "sl-class",
            "years": [{
                "id": 200739147,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401655566,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Mercedes_Benz_SLC_Class",
            "name": "SLC-Class",
            "niceName": "slc-class",
            "years": [{
                "id": 401612388,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW"]
        }, {
            "id": "Mercedes_Benz_SLK_Class",
            "name": "SLK-Class",
            "niceName": "slk-class",
            "years": [{
                "id": 200745344,
                "year": 2016,
                "states": ["NEW", "USED"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Mercedes_Benz_Sprinter",
            "name": "Sprinter",
            "niceName": "sprinter",
            "years": [{
                "id": 200779920,
                "year": 2016,
                "states": ["NEW", "USED"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Mercedes_Benz_Sprinter_Worker",
            "name": "Sprinter Worker",
            "niceName": "sprinter-worker",
            "years": [{
                "id": 401631621,
                "year": 2016,
                "states": ["NEW", "USED"]
            }],
            "states": ["NEW", "USED"]
        }]
    }, {
        "id": 200002915,
        "name": "Mitsubishi",
        "niceName": "mitsubishi",
        "models": [{
            "id": "Mitsubishi_Lancer",
            "name": "Lancer",
            "niceName": "lancer",
            "years": [{
                "id": 401582332,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401658210,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Mitsubishi_Lancer_Evolution",
            "name": "Lancer Evolution",
            "niceName": "lancer-evolution",
            "years": [{
                "id": 200713655,
                "year": 2015,
                "states": ["NEW", "USED"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Mitsubishi_Mirage",
            "name": "Mirage",
            "niceName": "mirage",
            "years": [{
                "id": 401638164,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Mitsubishi_Mirage_G4",
            "name": "Mirage G4",
            "niceName": "mirage-g4",
            "years": [{
                "id": 401637700,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW"]
        }, {
            "id": "Mitsubishi_Outlander",
            "name": "Outlander",
            "niceName": "outlander",
            "years": [{
                "id": 200734282,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401666428,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Mitsubishi_Outlander_Sport",
            "name": "Outlander Sport",
            "niceName": "outlander-sport",
            "years": [{
                "id": 401612355,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401677107,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Mitsubishi_i_MiEV",
            "name": "i-MiEV",
            "niceName": "i-miev",
            "years": [{
                "id": 200726943,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401643578,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }]
    }, {
        "id": 200000201,
        "name": "Nissan",
        "niceName": "nissan",
        "models": [{
            "id": "Nissan_370Z",
            "name": "370Z",
            "niceName": "370z",
            "years": [{
                "id": 200732068,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401647595,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Nissan_Altima",
            "name": "Altima",
            "niceName": "altima",
            "years": [{
                "id": 200737431,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401670609,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Nissan_Armada",
            "name": "Armada",
            "niceName": "armada",
            "years": [{
                "id": 401629994,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Nissan_Frontier",
            "name": "Frontier",
            "niceName": "frontier",
            "years": [{
                "id": 401581494,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401690338,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Nissan_GT_R",
            "name": "GT-R",
            "niceName": "gt-r",
            "years": [{
                "id": 200729794,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401648671,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Nissan_Juke",
            "name": "Juke",
            "niceName": "juke",
            "years": [{
                "id": 401612909,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401691449,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Nissan_Leaf",
            "name": "Leaf",
            "niceName": "leaf",
            "years": [{
                "id": 401610729,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401695946,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Nissan_Maxima",
            "name": "Maxima",
            "niceName": "maxima",
            "years": [{
                "id": 200719509,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401646961,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Nissan_Murano",
            "name": "Murano",
            "niceName": "murano",
            "years": [{
                "id": 401613849,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401677870,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Nissan_NV_Cargo",
            "name": "NV Cargo",
            "niceName": "nv-cargo",
            "years": [{
                "id": 401583839,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401695140,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Nissan_NV_Passenger",
            "name": "NV Passenger",
            "niceName": "nv-passenger",
            "years": [{
                "id": 401582661,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401693674,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Nissan_NV200",
            "name": "NV200",
            "niceName": "nv200",
            "years": [{
                "id": 401627754,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401671863,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Nissan_Pathfinder",
            "name": "Pathfinder",
            "niceName": "pathfinder",
            "years": [{
                "id": 401611671,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401667885,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Nissan_Quest",
            "name": "Quest",
            "niceName": "quest",
            "years": [{
                "id": 401610779,
                "year": 2016,
                "states": ["NEW", "USED"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Nissan_Rogue",
            "name": "Rogue",
            "niceName": "rogue",
            "years": [{
                "id": 401581354,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401689712,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Nissan_Rogue_Select",
            "name": "Rogue Select",
            "niceName": "rogue-select",
            "years": [{
                "id": 200726752,
                "year": 2015,
                "states": ["NEW", "USED"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Nissan_Sentra",
            "name": "Sentra",
            "niceName": "sentra",
            "years": [{
                "id": 401614164,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401678482,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Nissan_Titan",
            "name": "Titan",
            "niceName": "titan",
            "years": [{
                "id": 401638704,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Nissan_Titan_XD",
            "name": "Titan XD",
            "niceName": "titan-xd",
            "years": [{
                "id": 200691942,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401666732,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Nissan_Versa",
            "name": "Versa",
            "niceName": "versa",
            "years": [{
                "id": 200744978,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401667375,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Nissan_Versa_Note",
            "name": "Versa Note",
            "niceName": "versa-note",
            "years": [{
                "id": 200752583,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401692425,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }]
    }, {
        "id": 200000886,
        "name": "Porsche",
        "niceName": "porsche",
        "models": [{
            "id": "Porsche_718_Boxster",
            "name": "718 Boxster",
            "niceName": "718-boxster",
            "years": [{
                "id": 401627328,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW"]
        }, {
            "id": "Porsche_718_Cayman",
            "name": "718 Cayman",
            "niceName": "718-cayman",
            "years": [{
                "id": 401643316,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW"]
        }, {
            "id": "Porsche_911",
            "name": "911",
            "niceName": "911",
            "years": [{
                "id": 200729205,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401578403,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Porsche_Boxster",
            "name": "Boxster",
            "niceName": "boxster",
            "years": [{
                "id": 200731946,
                "year": 2016,
                "states": ["NEW", "USED"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Porsche_Cayenne",
            "name": "Cayenne",
            "niceName": "cayenne",
            "years": [{
                "id": 200732826,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401633797,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Porsche_Cayman",
            "name": "Cayman",
            "niceName": "cayman",
            "years": [{
                "id": 200729980,
                "year": 2016,
                "states": ["NEW", "USED"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Porsche_Macan",
            "name": "Macan",
            "niceName": "macan",
            "years": [{
                "id": 200731398,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401597832,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Porsche_Panamera",
            "name": "Panamera",
            "niceName": "panamera",
            "years": [{
                "id": 200734259,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401655426,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }]
    }, {
        "id": 200393150,
        "name": "Ram",
        "niceName": "ram",
        "models": [{
            "id": "Ram_1500",
            "name": "1500",
            "niceName": "1500",
            "years": [{
                "id": 200742272,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401655765,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Ram_2500",
            "name": "2500",
            "niceName": "2500",
            "years": [{
                "id": 200743476,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401630229,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "FUTURE", "USED"]
        }, {
            "id": "Ram_3500",
            "name": "3500",
            "niceName": "3500",
            "years": [{
                "id": 200743122,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401690971,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Ram_CV_Tradesman",
            "name": "CV Tradesman",
            "niceName": "cv-tradesman",
            "years": [{
                "id": 200705559,
                "year": 2015,
                "states": ["NEW", "USED"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Ram_Promaster_Cargo_Van",
            "name": "Promaster Cargo Van",
            "niceName": "promaster-cargo-van",
            "years": [{
                "id": 200734551,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401649492,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Ram_Promaster_City",
            "name": "Promaster City",
            "niceName": "promaster-city",
            "years": [{
                "id": 401582284,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401654857,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Ram_Promaster_Window_Van",
            "name": "Promaster Window Van",
            "niceName": "promaster-window-van",
            "years": [{
                "id": 200734214,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401660392,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }]
    }, {
        "id": 200005044,
        "name": "Rolls-Royce",
        "niceName": "rolls-royce",
        "models": [{
            "id": "Rolls_Royce_Dawn",
            "name": "Dawn",
            "niceName": "dawn",
            "years": [{
                "id": 401628476,
                "year": 2016,
                "states": ["NEW", "USED"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Rolls_Royce_Ghost_Series_II",
            "name": "Ghost Series II",
            "niceName": "ghost-series-ii",
            "years": [{
                "id": 401630684,
                "year": 2016,
                "states": ["NEW", "USED"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Rolls_Royce_Phantom",
            "name": "Phantom",
            "niceName": "phantom",
            "years": [{
                "id": 401629131,
                "year": 2016,
                "states": ["NEW", "USED"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Rolls_Royce_Phantom_Coupe",
            "name": "Phantom Coupe",
            "niceName": "phantom-coupe",
            "years": [{
                "id": 401627841,
                "year": 2016,
                "states": ["NEW", "USED"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Rolls_Royce_Phantom_Drophead_Coupe",
            "name": "Phantom Drophead Coupe",
            "niceName": "phantom-drophead-coupe",
            "years": [{
                "id": 401631105,
                "year": 2016,
                "states": ["NEW", "USED"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Rolls_Royce_Wraith",
            "name": "Wraith",
            "niceName": "wraith",
            "years": [{
                "id": 401629127,
                "year": 2016,
                "states": ["NEW", "USED"]
            }],
            "states": ["NEW", "USED"]
        }]
    }, {
        "id": 200006515,
        "name": "Scion",
        "niceName": "scion",
        "models": [{
            "id": "Scion_FR_S",
            "name": "FR-S",
            "niceName": "fr-s",
            "years": [{
                "id": 200734751,
                "year": 2016,
                "states": ["NEW", "USED"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Scion_iA",
            "name": "iA",
            "niceName": "ia",
            "years": [{
                "id": 200730054,
                "year": 2016,
                "states": ["NEW", "USED"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Scion_iM",
            "name": "iM",
            "niceName": "im",
            "years": [{
                "id": 200722068,
                "year": 2016,
                "states": ["NEW", "USED"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Scion_iQ",
            "name": "iQ",
            "niceName": "iq",
            "years": [{
                "id": 200709073,
                "year": 2015,
                "states": ["NEW", "USED"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Scion_tC",
            "name": "tC",
            "niceName": "tc",
            "years": [{
                "id": 200745612,
                "year": 2016,
                "states": ["NEW", "USED"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Scion_xB",
            "name": "xB",
            "niceName": "xb",
            "years": [{
                "id": 200722132,
                "year": 2015,
                "states": ["NEW", "USED"]
            }],
            "states": ["NEW", "USED"]
        }]
    }, {
        "id": 200004491,
        "name": "Subaru",
        "niceName": "subaru",
        "models": [{
            "id": "Subaru_BRZ",
            "name": "BRZ",
            "niceName": "brz",
            "years": [{
                "id": 200772765,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401659390,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Subaru_Crosstrek",
            "name": "Crosstrek",
            "niceName": "crosstrek",
            "years": [{
                "id": 401575886,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401678670,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Subaru_Forester",
            "name": "Forester",
            "niceName": "forester",
            "years": [{
                "id": 200740435,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401645884,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Subaru_Impreza",
            "name": "Impreza",
            "niceName": "impreza",
            "years": [{
                "id": 401574186,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401597110,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "FUTURE", "USED"]
        }, {
            "id": "Subaru_Legacy",
            "name": "Legacy",
            "niceName": "legacy",
            "years": [{
                "id": 200738270,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401646454,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Subaru_Outback",
            "name": "Outback",
            "niceName": "outback",
            "years": [{
                "id": 200738662,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401646453,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Subaru_WRX",
            "name": "WRX",
            "niceName": "wrx",
            "years": [{
                "id": 200733182,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401645640,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }]
    }, {
        "id": 200018920,
        "name": "Tesla",
        "niceName": "tesla",
        "models": [{
            "id": "Tesla_Model_S",
            "name": "Model S",
            "niceName": "model-s",
            "years": [{
                "id": 401632873,
                "year": 2016,
                "states": ["NEW", "USED"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Tesla_Model_X",
            "name": "Model X",
            "niceName": "model-x",
            "years": [{
                "id": 200720386,
                "year": 2016,
                "states": ["NEW", "USED"]
            }],
            "states": ["NEW", "USED"]
        }]
    }, {
        "id": 200003381,
        "name": "Toyota",
        "niceName": "toyota",
        "models": [{
            "id": "Toyota_4Runner",
            "name": "4Runner",
            "niceName": "4runner",
            "years": [{
                "id": 200747158,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401694837,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Toyota_86",
            "name": "86",
            "niceName": "86",
            "years": [{
                "id": 401628160,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW"]
        }, {
            "id": "Toyota_Avalon",
            "name": "Avalon",
            "niceName": "avalon",
            "years": [{
                "id": 401583408,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401689572,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Toyota_Avalon_Hybrid",
            "name": "Avalon Hybrid",
            "niceName": "avalon-hybrid",
            "years": [{
                "id": 401583409,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401678607,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Toyota_Camry",
            "name": "Camry",
            "niceName": "camry",
            "years": [{
                "id": 200746613,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401647948,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Toyota_Camry_Hybrid",
            "name": "Camry Hybrid",
            "niceName": "camry-hybrid",
            "years": [{
                "id": 200747124,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401647949,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Toyota_Corolla",
            "name": "Corolla",
            "niceName": "corolla",
            "years": [{
                "id": 200746612,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401668008,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Toyota_Corolla_iM",
            "name": "Corolla iM",
            "niceName": "corolla-im",
            "years": [{
                "id": 401628158,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW"]
        }, {
            "id": "Toyota_Highlander",
            "name": "Highlander",
            "niceName": "highlander",
            "years": [{
                "id": 401596890,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401633259,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "FUTURE", "USED"]
        }, {
            "id": "Toyota_Highlander_Hybrid",
            "name": "Highlander Hybrid",
            "niceName": "highlander-hybrid",
            "years": [{
                "id": 401596891,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401694319,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Toyota_Land_Cruiser",
            "name": "Land Cruiser",
            "niceName": "land-cruiser",
            "years": [{
                "id": 401581941,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401659091,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Toyota_Mirai",
            "name": "Mirai",
            "niceName": "mirai",
            "years": [{
                "id": 200711329,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401689571,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Toyota_Prius",
            "name": "Prius",
            "niceName": "prius",
            "years": [{
                "id": 200706801,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401658851,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Toyota_Prius_Prime",
            "name": "Prius Prime",
            "niceName": "prius-prime",
            "years": [{
                "id": 401649189,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "FUTURE"]
        }, {
            "id": "Toyota_Prius_c",
            "name": "Prius c",
            "niceName": "prius-c",
            "years": [{
                "id": 401597745,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401694839,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Toyota_Prius_v",
            "name": "Prius v",
            "niceName": "prius-v",
            "years": [{
                "id": 200748018,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401641255,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Toyota_RAV4",
            "name": "RAV4",
            "niceName": "rav4",
            "years": [{
                "id": 200731829,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401658883,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Toyota_RAV4_Hybrid",
            "name": "RAV4 Hybrid",
            "niceName": "rav4-hybrid",
            "years": [{
                "id": 401598559,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401658945,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Toyota_Sequoia",
            "name": "Sequoia",
            "niceName": "sequoia",
            "years": [{
                "id": 401566717,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401690560,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Toyota_Sienna",
            "name": "Sienna",
            "niceName": "sienna",
            "years": [{
                "id": 401611598,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401659111,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Toyota_Tacoma",
            "name": "Tacoma",
            "niceName": "tacoma",
            "years": [{
                "id": 200722298,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401659110,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Toyota_Tundra",
            "name": "Tundra",
            "niceName": "tundra",
            "years": [{
                "id": 200771502,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401671449,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Toyota_Yaris",
            "name": "Yaris",
            "niceName": "yaris",
            "years": [{
                "id": 401598558,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401659058,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Toyota_Yaris_iA",
            "name": "Yaris iA",
            "niceName": "yaris-ia",
            "years": [{
                "id": 401628159,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW"]
        }]
    }, {
        "id": 200000238,
        "name": "Volkswagen",
        "niceName": "volkswagen",
        "models": [{
            "id": "Volkswagen_Beetle",
            "name": "Beetle",
            "niceName": "beetle",
            "years": [{
                "id": 401575740,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401691519,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Volkswagen_Beetle_Convertible",
            "name": "Beetle Convertible",
            "niceName": "beetle-convertible",
            "years": [{
                "id": 401578621,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401691520,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Volkswagen_CC",
            "name": "CC",
            "niceName": "cc",
            "years": [{
                "id": 401593704,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401666499,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Volkswagen_Eos",
            "name": "Eos",
            "niceName": "eos",
            "years": [{
                "id": 200771658,
                "year": 2016,
                "states": ["NEW", "USED"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Volkswagen_Golf",
            "name": "Golf",
            "niceName": "golf",
            "years": [{
                "id": 401572276,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401665871,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Volkswagen_Golf_Alltrack",
            "name": "Golf Alltrack",
            "niceName": "golf-alltrack",
            "years": [{
                "id": 200731841,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "FUTURE"]
        }, {
            "id": "Volkswagen_Golf_GTI",
            "name": "Golf GTI",
            "niceName": "golf-gti",
            "years": [{
                "id": 200751185,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401665935,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Volkswagen_Golf_R",
            "name": "Golf R",
            "niceName": "golf-r",
            "years": [{
                "id": 200749648,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401665996,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Volkswagen_Golf_SportWagen",
            "name": "Golf SportWagen",
            "niceName": "golf-sportwagen",
            "years": [{
                "id": 401572277,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401666026,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Volkswagen_Jetta",
            "name": "Jetta",
            "niceName": "jetta",
            "years": [{
                "id": 401575136,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401666227,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Volkswagen_Passat",
            "name": "Passat",
            "niceName": "passat",
            "years": [{
                "id": 401589418,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401666332,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Volkswagen_Tiguan",
            "name": "Tiguan",
            "niceName": "tiguan",
            "years": [{
                "id": 200749526,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401578392,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Volkswagen_Touareg",
            "name": "Touareg",
            "niceName": "touareg",
            "years": [{
                "id": 200759788,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401666615,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Volkswagen_e_Golf",
            "name": "e-Golf",
            "niceName": "e-golf",
            "years": [{
                "id": 401597166,
                "year": 2016,
                "states": ["NEW", "USED"]
            }],
            "states": ["NEW", "USED"]
        }]
    }, {
        "id": 200010382,
        "name": "Volvo",
        "niceName": "volvo",
        "models": [{
            "id": "Volvo_S60",
            "name": "S60",
            "niceName": "s60",
            "years": [{
                "id": 200737680,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401660136,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Volvo_S60_Cross_Country",
            "name": "S60 Cross Country",
            "niceName": "s60-cross-country",
            "years": [{
                "id": 401660113,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW"]
        }, {
            "id": "Volvo_S80",
            "name": "S80",
            "niceName": "s80",
            "years": [{
                "id": 200737889,
                "year": 2016,
                "states": ["NEW", "USED"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Volvo_S90",
            "name": "S90",
            "niceName": "s90",
            "years": [{
                "id": 401588247,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Volvo_V60",
            "name": "V60",
            "niceName": "v60",
            "years": [{
                "id": 200737643,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401659019,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Volvo_V60_Cross_Country",
            "name": "V60 Cross Country",
            "niceName": "v60-cross-country",
            "years": [{
                "id": 200737895,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401659666,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Volvo_V90_Cross_Country",
            "name": "V90 Cross Country",
            "niceName": "v90-cross-country",
            "years": [{
                "id": 401689298,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "FUTURE"]
        }, {
            "id": "Volvo_XC60",
            "name": "XC60",
            "niceName": "xc60",
            "years": [{
                "id": 200737697,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401657921,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Volvo_XC70",
            "name": "XC70",
            "niceName": "xc70",
            "years": [{
                "id": 200739112,
                "year": 2016,
                "states": ["NEW", "USED"]
            }],
            "states": ["NEW", "USED"]
        }, {
            "id": "Volvo_XC90",
            "name": "XC90",
            "niceName": "xc90",
            "years": [{
                "id": 200711225,
                "year": 2016,
                "states": ["NEW", "USED"]
            }, {
                "id": 401657970,
                "year": 2017,
                "states": ["NEW"]
            }],
            "states": ["NEW", "USED"]
        }]
    }, {
        "id": 200038885,
        "name": "smart",
        "niceName": "smart",
        "models": [{
            "id": "smart_fortwo",
            "name": "fortwo",
            "niceName": "fortwo",
            "years": [{
                "id": 200705423,
                "year": 2016,
                "states": ["NEW", "USED"]
            }],
            "states": ["NEW", "USED"]
        }]
    }],
    "makesCount": 44
}





count=0
for i in (modelsdict['makes']):
    print (i['niceName']);
    for j in i['models']:
        print ("       "+j['niceName']);
        for k in j['years']:
            print ("             "+str(k['year'])+"-"+str(k['id']));
            data_model = (i['niceName'],j['niceName'],k['year'],k['id'])
            cursor.execute(add_model,data_model)
            count+=1
print (count)
'''




cnx.commit()

cursor.close()
cnx.close()

