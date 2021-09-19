import requests
from bs4 import BeautifulSoup

# url Aesch Ag [1, 40, 83, 104, 122, 140, 160, 167, 184, 192, 205, 218, 228, 238, 248, 258, 281, 320, 355, 367, 385, 403, 420, 437, 456, 475, 488, 538, 583, 613, 636, 681, 699, 716, 727, 737, 750, 763, 772, 782, 810, 855, 887, 914, 944, 975, 988, 1001, 1017, 1035, 1072, 1076, 1080, 1085, 1090, 1095, 1100, 1107, 1114, 1125, 1136, 1146, 1156, 1167, 1178, 1202, 1242, 1295, 1331, 1343, 1344, 1345, 1346, 1348, 1372, 1407, 1412, 1426, 1431, 1448, 1455, 1462, 1468, 1475, 1481, 1489, 1497, 1505, 1513, 1521, 1531, 1537, 1551, 1560, 1567, 1577, 1617, 1649]
# pages Aesch Ag 'http://www.perseus.tufts.edu/hopper/text?doc=Perseus%3Atext%3A1999.01.0003%3Acard%3D'
# url Aesch Eu 'http://www.perseus.tufts.edu/hopper/text?doc=Perseus%3Atext%3A1999.01.0005%3Acard%3D'
# pages Aesch Eu [' 1', '34', '64', '94', '131', '143', '149', '155', '162', '169', '174', '178', '213', '254', '276', '299', '307', '321', '328', '334', '341', '347', '354', '360', '354a', '368', '372', '377', '372a', '381', '389', '397', '436', '470', '490', '499', '508', '517', '526', '538', '550', '558', '566', '607', '640', '674', '711', '744', '778', '793', '808', '823', '837', '848', '870', '881', '916', '927', '938', '949', '956', '968', '976', '988', '996', '1003', '1014', '1021', '1032', '1035', '1040', '1044 ']
# url Aesch Choe 'http://www.perseus.tufts.edu/hopper/text?doc=Perseus%3Atext%3A1999.01.0007%3Acard%3D'
# pages Aesch Choe [' 1', '22', '32', '42', '55', '66', '71', '75', '84', '106', '152', '164', '195', '225', '264', '306', '315', '323', '332', '340', '345', '354', '363', '372', '380', '386', '394', '400', '405', '410', '418', '423', '429', '434', '439', '445', '451', '456', '461', '466', '471', '476', '479', '510', '540', '585', '594', '602', '612', '623', '631', '639', '646', '653', '691', '719', '730', '766', '783', '789', '794', '800', '806', '811', '819', '827', '831', '838', '855', '869', '875', '900', '935', '942', 'line 946', '942a', '953', '961', '966', '972', '973', '1007', '1010', '1018', '1021', '1051', '1065 ']
# url Aesch Pers 'http://www.perseus.tufts.edu/hopper/text?doc=Perseus%3Atext%3A1999.01.0011%3Acard%3D'
# pages Aesch Pers [' 1', '41', '65', '73', '81', '87', '93', '100', '107', '111', '115', '120', '126', '133', '140', '155', '159', '176', '200', '215', '232', '249', '256', '260', '262', '266', '268', '272', '274', '278', '280', '284', '286', '290', '331', '353', '395', '433', '472', '480', '515', '532', '548', '558', '568', '576', '584', '591', '598', '623', '633', '640', '647', '652', '657', '664', '673', '681', '694', '697', '700', '703', '715', '739', '759', '787', '800', '843', '852', '858', '864', '871', '879', '889', '898', '909', '932', '941', '950', '962', '974', '988', '1002', '1008', '1014', '1026', '1038', '1046', '1054', '1060', '1066 ']
# url Aesch Prom 'http://www.perseus.tufts.edu/hopper/text?doc=Perseus%3Atext%3A1999.01.0009%3Acard%3D'
# pages Aesch Prom [' 1', '36', '61', '88', '95', '101', '114', '121', '128', '136', '144', '152', '160', '168', '180', '189', '196', '244', '265', '279', '300', '332', '343', '379', '399', '407', '415', '420', '425', '436', '472', '507', '526', '537', '545', '552', '561', '566', '575', '589', '593', '609', '640', '687', '696', '742', '780', '819', '846', '877', '887', '894', '901', '907', '944', '964', '1007', '1040', '1080 ']
# url Aesch Sept 'http://www.perseus.tufts.edu/hopper/text?doc=Perseus%3Atext%3A1999.01.0013%3Acard%3D'
# pages Aesch Sept [' 1', '39', '78', '109', '128', '149', '158', '166', '174', '181', '203', '211', '219', '226', '233', '239', '245', '288', '304', '321', '333', '345', '357', '369', '417', '422', '452', '457', '481', '486', '521', '526', '563', '568', '626', '631', '686', '692', '698', '705', '712', '720', '727', '734', '742', '750', '758', '766', '772', '778', '785', '792', '822', '833', '840', '848', '875', '881', '888', '900', '911', '922', '933', '945', '957', '966', '980', '994', '1011', '1032', '1048 ']
# url Aesch Hik 'http://www.perseus.tufts.edu/hopper/text?doc=Perseus%3Atext%3A1999.01.0015%3Acard%3D'
# pages Aesch Hik [' 1', '40', '49', '58', '63', '68', '77', '86', '91', '96', '104', '112', '117', '123', '128', '134', '141', '144', '151', '154', '162', '168', '162a', '176', '207', '234', '274', '291', '323', '348', '354', '359', '365', '370', '376', '381', '387', '392', '397', '402', '407', '418', '423', '428', '433', '438', '490', '524', '531', '538', '547', '556', '565', '574', '582', '590', '595', '600', '625', '630', '643', '656', '667', '678', '688', '698', '704', '710', '736', '739', '743', '746', '750', '753', '757', '760', '776', '784', '792', '800', '808', '817', '825', '836', '843', '849', '854', '861', '866', '872', '876', '882', '885', '893', '895', '902', '930', '966', '980', '1018', '1026', '1034', '1043', '1052', '1057', '1062', '1068 ']

pages = [' 1', '40', '49', '58', '63', '68', '77', '86', '91', '96', '104', '112', '117', '123', '128', '134', '141', '144', '151', '154', '162', '168', '162a', '176', '207', '234', '274', '291', '323', '348', '354', '359', '365', '370', '376', '381', '387', '392', '397', '402', '407', '418', '423', '428', '433', '438', '490', '524', '531', '538', '547', '556', '565', '574', '582', '590', '595', '600', '625', '630', '643', '656', '667', '678', '688', '698', '704', '710', '736', '739', '743', '746', '750', '753', '757', '760', '776', '784', '792', '800', '808', '817', '825', '836', '843', '849', '854', '861', '866', '872', '876', '882', '885', '893', '895', '902', '930', '966', '980', '1018', '1026', '1034', '1043', '1052', '1057', '1062', '1068 ']
url = 'http://www.perseus.tufts.edu/hopper/text?doc=Perseus%3Atext%3A1999.01.0015%3Acard%3D'

def getContent(page, url):
    word_list = []
    URL = url + page
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find_all("a", class_="text")
    for result in results:
        word_list.append(result.text)
    return word_list

new_result = []
for page in pages:
    new_result.append(getContent(page, url))
    

with open('aeschylusHik.txt', 'w') as file:
    file.write(str(new_result))