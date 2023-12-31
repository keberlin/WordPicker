from search import gen_match, search, search2


def test_gen_match():
    result = gen_match("PAYER", "P.Y.R")
    assert result == ".A.E."


def test_rack(client):
    matches = search("KEITHY", None)
    results = [
        "EH",
        "EIK",
        "ET",
        "ETH",
        "HE",
        "HET",
        "HEY",
        "HI",
        "HIE",
        "HIKE",
        "HIT",
        "HYE",
        "HYKE",
        "HYTE",
        "IT",
        "KET",
        "KEY",
        "KHET",
        "KHI",
        "KI",
        "KIT",
        "KITE",
        "KITH",
        "KITHE",
        "KY",
        "KYE",
        "KYTE",
        "KYTHE",
        "TE",
        "THE",
        "THEY",
        "THY",
        "TI",
        "TIE",
        "TIKE",
        "TYE",
        "TYKE",
        "YE",
        "YEH",
        "YET",
        "YETI",
        "YIKE",
        "YITE",
    ]
    assert matches == results


def test_rack_with_blanks(client):
    matches = search("P.X", None)
    results = [
        "AX",
        "EX",
        "OP",
        "OX",
        "PA",
        "PAX",
        "PE",
        "PI",
        "PIX",
        "PO",
        "POX",
        "PYX",
        "UP",
        "XI",
        "XU",
    ]
    assert matches == results


def test_rack_with_blanks_and_pattern(client):
    matches = search("P.R.", "P.R.")
    results = [
        "APPRO",
        "PARA",
        "PARD",
        "PARE",
        "PARER",
        "PARK",
        "PARP",
        "PARPS",
        "PARR",
        "PARRA",
        "PARRS",
        "PARRY",
        "PARS",
        "PART",
        "PERE",
        "PERI",
        "PERK",
        "PERM",
        "PERN",
        "PERP",
        "PERPS",
        "PERRY",
        "PERT",
        "PERV",
        "PIRL",
        "PIRN",
        "PIRS",
        "PORE",
        "PORER",
        "PORK",
        "PORN",
        "PORT",
        "PORY",
        "PURE",
        "PURER",
        "PURI",
        "PURL",
        "PURPY",
        "PURR",
        "PURRS",
        "PURS",
        "PYRE",
        "PYRO",
    ]
    assert matches == results


def test_rack_with_pattern_1(client):
    matches = search("KEITHY", "TH")
    results = [
        "ETH",
        "HETH",
        "HITHE",
        "HYTHE",
        "KHETH",
        "KITH",
        "KITHE",
        "KYTHE",
        "TETH",
        "THE",
        "THEY",
        "THY",
        "TITHE",
        "TYTHE",
    ]
    assert matches == results


def test_rack_with_pattern_2(client):
    matches = search("GAME", "D")
    results = [
        "AD",
        "AGED",
        "DA",
        "DAE",
        "DAG",
        "DAM",
        "DAME",
        "DE",
        "DEG",
        "ED",
        "EGAD",
        "GAD",
        "GADE",
        "GAED",
        "GAMED",
        "GED",
        "MAD",
        "MADE",
        "MADGE",
        "MEAD",
        "MED",
    ]
    assert matches == results


def test_rack_with_pattern_3(client):
    matches = search("KEITH", "$...$")
    results = ["EIK", "ETH", "HET", "HIE", "HIT", "KET", "KHI", "KIT", "THE", "TIE"]
    assert matches == results


def test_pattern(client):
    matches = search("", "$AZON")
    results = ["AZON", "AZONAL", "AZONIC", "AZONS"]
    assert matches == results


def test_rack_with_multi_pattern(client):
    matches = search2("CHELSAY", ["$...$", "$....$"])
    results = [
        "ACH LEYS",
        "ACH LYES",
        "ACH LYSE",
        "ACH SLEY",
        "ALS YECH",
        "AYS LECH",
        "CEL ASHY",
        "CEL HAYS",
        "CEL SHAY",
        "CEL YAHS",
        "CHA LEYS",
        "CHA LYES",
        "CHA LYSE",
        "CHA SLEY",
        "CHE LAYS",
        "CHE SLAY",
        "CLY HAES",
        "CLY SHEA",
        "EAS LYCH",
        "ECH LAYS",
        "ECH SLAY",
        "EHS ACYL",
        "EHS CLAY",
        "EHS LACY",
        "ELS ACHY",
        "ELS CHAY",
        "HAY CELS",
        "HES ACYL",
        "HES CLAY",
        "HES LACY",
        "HEY LACS",
        "HYE LACS",
        "LAC HEYS",
        "LAC HYES",
        "LAH SCYE",
        "LAH SYCE",
        "LAS YECH",
        "LAY SECH",
        "LES ACHY",
        "LES CHAY",
        "LEY CASH",
        "LEY CHAS",
        "LYE CASH",
        "LYE CHAS",
        "SAC HYLE",
        "SAE LYCH",
        "SAL YECH",
        "SAY LECH",
        "SEA LYCH",
        "SEC HYLA",
        "SEL ACHY",
        "SEL CHAY",
        "SEY CHAL",
        "SHE ACYL",
        "SHE CLAY",
        "SHE LACY",
        "SHY ALEC",
        "SHY LACE",
        "SLY ACHE",
        "SLY EACH",
        "SYE CHAL",
        "YAH CELS",
        "YEH LACS",
        "YES CHAL",
    ]
    assert matches == results
