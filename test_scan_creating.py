import pytest
from scans_generator import generate
from map_model import Map


@pytest.fixture
def local_map():
    return Map(debug=True)


def test_positions_creating(local_map):
    positions = local_map.get_free_positions()
    correct_positions_for_local_map = [(1.5, 0.5, 0),
                                       (2.5, 0.5, 0),
                                       (3.5, 0.5, 0),
                                       (4.5, 0.5, 0),
                                       (1.5, 1.5, 0),
                                       (2.5, 1.5, 0),
                                       (4.5, 1.5, 0),
                                       (1.5, 2.5, 0),
                                       (2.5, 2.5, 0),
                                       (3.5, 2.5, 0),
                                       (4.5, 2.5, 0),
                                       (0.5, 3.5, 0),
                                       (1.5, 3.5, 0),
                                       (2.5, 3.5, 0),
                                       (3.5, 3.5, 0),
                                       (4.5, 3.5, 0),
                                       (0.5, 4.5, 0),
                                       (1.5, 4.5, 0),
                                       (2.5, 4.5, 0)]
    assert positions == correct_positions_for_local_map


def test_scans_creating(local_map):
    positions = local_map.get_free_positions()
    correct_scans = [
        {0: (1.0, 0.5), 10: (1.0, 0.5881634903542325), 20: (1.0, 0.6819851171331015), 30: (1.0, 0.7886751345948131),
         40: (1.0, 0.9195498155886401), 50: (1.0000000000000002, 1.0958767962971048), 60: (1.0, 1.3660254037844384),
         70: (0.9999999999999999, 1.8737387097273106), 80: (0.7065285868119073, 5.0), 90: (1.5, 0.0),
         100: (1.4118365096457675, 0.0), 110: (1.3180148828668992, 0.0), 120: (1.2113248654051876, 0.0),
         130: (1.0804501844113603, 0.0), 140: (1.0, 0.08045018441135987), 150: (1.0, 0.2113248654051869),
         160: (1.0, 0.3180148828668994), 170: (1.0, 0.41183650964576746), 180: (5.0, 0.4999999999999996),
         190: (4.335640909808852, 0.0), 200: (2.873738709727312, 0.0), 210: (2.3660254037844384, 0.0),
         220: (2.0958767962971048, 0.0), 230: (1.9195498155886401, 0.0), 240: (1.7886751345948133, 0.0),
         250: (1.6819851171331015, 0.0), 260: (1.5881634903542323, 0.0), 270: (1.5, 5.0),
         280: (2.2934714131880907, 5.0), 290: (3.0000000000000004, 4.62121612918193), 300: (3.5207259421636903, 4.0),
         310: (4.43684870912048, 4.0), 320: (3.0, 1.7586494467659213), 330: (3.0, 1.3660254037844402),
         340: (3.0, 1.045955351399305), 350: (5.0, 1.1171444324796278)},
        {0: (1.0, 0.5), 10: (1.0, 0.7644904710626976), 20: (1.0, 1.0459553513993036), 30: (1.0, 1.3660254037844384),
         40: (1.0, 1.75864944676592), 50: (0.9999999999999998, 2.2876303888913148), 60: (-0.0, 4.830127018922192),
         70: (0.8621339458020889, 5.0), 80: (1.7065285868119073, 5.0), 90: (2.5, 0.0), 100: (2.4118365096457675, 0.0),
         110: (2.318014882866899, 0.0), 120: (2.2113248654051865, 0.0), 130: (2.0804501844113608, 0.0),
         140: (1.904123203702895, 0.0), 150: (1.6339745962155605, 0.0), 160: (1.1262612902726903, 0.0),
         170: (1.0, 0.23550952893730148), 180: (5.0, 0.4999999999999997), 190: (5.0, 0.059182548228837284),
         200: (3.8737387097273115, 0.0), 210: (3.3660254037844384, 0.0), 220: (3.095876796297105, 0.0),
         230: (2.91954981558864, 0.0), 240: (2.7886751345948135, 0.0), 250: (2.6819851171331015, 0.0),
         260: (2.5881634903542325, 0.0), 270: (2.5, 5.0), 280: (3.117144432479626, 4.0),
         290: (3.0000000000000004, 1.873738709727311), 300: (3.0000000000000004, 1.3660254037844388),
         310: (3.0, 1.0958767962971048), 320: (3.095876796297104, 1.0), 330: (3.3660254037844375, 1.0),
         340: (3.8737387097273075, 1.0), 350: (5.0, 0.9408174517711627)},
        {0: (1.0, 0.5), 10: (1.0, 0.9408174517711627), 20: (1.0, 1.4099255856655057), 30: (1.0, 1.943375672974064),
         40: (1.0, 2.5977490779431993), 50: (3.0804501844113594, 1.0), 60: (3.211324865405187, 1.0),
         70: (3.3180148828668985, 1.0), 80: (3.411836509645768, 1.0), 90: (3.5, 0.0), 100: (3.4118365096457675, 0.0),
         110: (3.318014882866899, 0.0), 120: (3.211324865405187, 0.0), 130: (3.0804501844113608, 0.0),
         140: (2.904123203702895, 0.0), 150: (2.6339745962155616, 0.0), 160: (2.126261290272689, 0.0),
         170: (1.0, 0.059182548228836396), 180: (5.0, 0.49999999999999983), 190: (5.0, 0.23550952893730237),
         200: (4.873738709727311, 0.0), 210: (4.366025403784438, 0.0), 220: (4.095876796297105, 0.0),
         230: (3.9195498155886406, 0.0), 240: (3.788675134594813, 0.0), 250: (3.681985117133101, 0.0),
         260: (3.5881634903542325, 0.0), 270: (3.5, 1.0), 280: (3.588163490354232, 1.0), 290: (3.6819851171331015, 1.0),
         300: (3.7886751345948126, 1.0), 310: (3.9195498155886406, 1.0), 320: (5.0, 1.7586494467659204),
         330: (5.0, 1.3660254037844393), 340: (5.0, 1.045955351399304), 350: (5.0, 0.7644904710626976)},
        {0: (1.0, 0.5), 10: (1.0, 1.1171444324796274), 20: (3.1262612902726885, 1.0), 30: (3.6339745962155607, 1.0),
         40: (3.9041232037028952, 1.0), 50: (4.0, 1.0958767962971052), 60: (4.0, 1.3660254037844384),
         70: (4.0, 1.873738709727312), 80: (3.882855567520372, 4.0), 90: (4.5, 0.0), 100: (4.4118365096457675, 0.0),
         110: (4.3180148828668985, 0.0), 120: (4.211324865405187, 0.0), 130: (4.080450184411361, 0.0),
         140: (3.904123203702895, 0.0), 150: (3.6339745962155607, 0.0), 160: (3.1262612902726903, 0.0),
         170: (1.6643590901911498, 0.0), 180: (5.0, 0.49999999999999994), 190: (5.0, 0.41183650964576746),
         200: (5.0, 0.3180148828668985), 210: (5.0, 0.2113248654051869), 220: (5.0, 0.08045018441135987),
         230: (4.91954981558864, 0.0), 240: (4.788675134594813, 0.0), 250: (4.6819851171331015, 0.0),
         260: (4.5881634903542325, 0.0), 270: (4.5, 4.0), 280: (5.000000000000001, 3.335640909808863),
         290: (5.0, 1.873738709727311), 300: (5.0, 1.3660254037844375), 310: (5.000000000000001, 1.0958767962971048),
         320: (5.0, 0.9195498155886392), 330: (5.0, 0.7886751345948131), 340: (5.0, 0.6819851171331006),
         350: (5.0, 0.5881634903542325)},
        {0: (1.0, 1.5), 10: (1.0, 1.5881634903542325), 20: (1.0, 1.6819851171331015), 30: (1.0, 1.7886751345948126),
         40: (1.0, 1.9195498155886397), 50: (1.0000000000000002, 2.0958767962971048), 60: (1.0, 2.3660254037844384),
         70: (1.0, 2.87373870972731), 80: (0.8828555675203724, 5.0), 90: (1.5, 0.0), 100: (1.2355095289373026, 0.0),
         110: (0.9999999999999999, 0.12626129027268806), 120: (1.0000000000000002, 0.6339745962155607),
         130: (0.9999999999999994, 0.9041232037028939), 140: (1.0, 1.0804501844113599), 150: (1.0, 1.2113248654051874),
         160: (1.0, 1.318014882866899), 170: (1.0, 1.4118365096457675), 180: (3.0, 1.4999999999999998),
         190: (3.0, 1.2355095289373024), 200: (3.0, 0.9540446486006964), 210: (4.098076211353315, 0.0),
         220: (3.287630388891315, 0.0), 230: (2.7586494467659204, 0.0), 240: (2.3660254037844397, 0.0),
         250: (2.0459553513993045, 0.0), 260: (1.7644904710626974, 0.0), 270: (1.5, 5.0), 280: (2.117144432479626, 5.0),
         290: (2.7738958199317096, 5.0), 300: (2.9999999999999996, 4.098076211353315), 310: (3.5977490779431998, 4.0),
         320: (4.4793839814855225, 4.0), 330: (5.0, 3.5207259421636934), 340: (3.0, 2.045955351399305),
         350: (3.0, 1.7644904710626976)},
        {0: (1.0, 1.5), 10: (1.0, 1.7644904710626972), 20: (1.0, 2.0459553513993036), 30: (1.0, 2.3660254037844384),
         40: (1.0, 2.75864944676592), 50: (-0.0, 4.479383981485524), 60: (0.47927405783630916, 5.0),
         70: (1.2261041800682915, 5.0), 80: (1.8828555675203724, 5.0), 90: (2.5, 0.0), 100: (2.235509528937303, 0.0),
         110: (1.9540446486006968, 0.0), 120: (1.6339745962155616, 0.0), 130: (1.2413505532340807, 0.0),
         140: (1.0, 0.2413505532340796), 150: (1.0, 0.6339745962155616), 160: (1.0, 0.9540446486006964),
         170: (1.0, 1.2355095289373024), 180: (3.0, 1.4999999999999998), 190: (3.0, 1.4118365096457675),
         200: (3.0, 1.318014882866899), 210: (3.0, 1.211324865405187), 220: (3.0, 1.0804501844113603),
         230: (3.758649446765921, 0.0), 240: (3.3660254037844397, 0.0), 250: (3.0459553513993045, 0.0),
         260: (2.7644904710626976, 0.0), 270: (2.5, 5.0), 280: (3.0, 4.3356409098088635),
         290: (3.4099255856655066, 4.0), 300: (3.9433756729740645, 4.0), 310: (4.5977490779432, 4.0),
         320: (3.0, 1.919549815588641), 330: (3.0, 1.788675134594813), 340: (3.0, 1.681985117133102),
         350: (3.0, 1.5881634903542325)},
        {0: (4.0, 1.5), 10: (4.0, 1.5881634903542325), 20: (4.0, 1.681985117133101), 30: (4.0, 1.7886751345948126),
         40: (4.0, 1.9195498155886401), 50: (1.5631512908795198, 5.0), 60: (3.056624327025935, 4.0),
         70: (3.590074414334494, 4.0), 80: (4.059182548228837, 4.0), 90: (4.5, 0.0), 100: (4.235509528937302, 0.0),
         110: (3.9540446486006964, 0.0), 120: (3.6339745962155616, 0.0), 130: (3.241350553234081, 0.0),
         140: (4.0, 1.0804501844113603), 150: (4.0, 1.2113248654051874), 160: (4.0, 1.3180148828668985),
         170: (4.0, 1.4118365096457675), 180: (5.0, 1.4999999999999998), 190: (5.0, 1.4118365096457675),
         200: (5.0, 1.3180148828668985), 210: (5.0, 1.211324865405187), 220: (5.0, 1.0804501844113599),
         230: (5.0, 0.9041232037028948), 240: (4.999999999999999, 0.6339745962155625), 250: (5.0, 0.12626129027269162),
         260: (4.764490471062698, 0.0), 270: (4.5, 4.0), 280: (4.940817451771162, 4.0), 290: (5.0, 2.8737387097273097),
         300: (5.0, 2.3660254037844366), 310: (5.0, 2.0958767962971043), 320: (5.0, 1.9195498155886401),
         330: (5.0, 1.788675134594813), 340: (5.0, 1.681985117133101), 350: (5.0, 1.5881634903542325)},
        {0: (1.0, 2.5), 10: (1.0, 2.5881634903542325), 20: (1.0, 2.6819851171331015), 30: (1.0, 2.7886751345948126),
         40: (1.0, 2.91954981558864), 50: (-0.0, 4.287630388891315), 60: (0.05662432702593514, 5.0),
         70: (0.5900744143344936, 5.0), 80: (1.0591825482288375, 5.0), 90: (1.5, 0.0), 100: (1.0591825482288377, 0.0),
         110: (0.9999999999999999, 1.126261290272688), 120: (0.9999999999999999, 1.6339745962155603),
         130: (1.0000000000000002, 1.9041232037028948), 140: (1.0, 2.08045018441136), 150: (1.0, 2.2113248654051874),
         160: (1.0, 2.318014882866899), 170: (1.0, 2.4118365096457675), 180: (5.0, 2.4999999999999996),
         190: (5.0, 1.8828555675203722), 200: (3.0, 1.9540446486006964), 210: (3.0, 1.6339745962155607),
         220: (3.0, 1.2413505532340805), 230: (3.597749077943201, 0.0), 240: (2.943375672974066, 0.0),
         250: (2.4099255856655075, 0.0), 260: (1.9408174517711623, 0.0), 270: (1.5, 5.0),
         280: (1.9408174517711616, 5.0), 290: (2.409925585665507, 5.0), 300: (2.9433756729740645, 5.0),
         310: (3.0, 4.287630388891315), 320: (3.287630388891314, 4.0), 330: (4.0980762113533125, 4.0),
         340: (5.0, 3.773895819931711), 350: (5.0, 3.117144432479628)},
        {0: (1.0, 2.5), 10: (1.0, 2.764490471062697), 20: (1.0, 3.0459553513993036), 30: (0.0, 3.943375672974064),
         40: (0.0, 4.5977490779432), 50: (0.4022509220567995, 5.0), 60: (1.0566243270259352, 5.0),
         70: (1.5900744143344938, 5.0), 80: (2.0591825482288373, 5.0), 90: (2.5, 0.0), 100: (2.0591825482288377, 0.0),
         110: (1.5900744143344945, 0.0), 120: (1.0566243270259363, 0.0), 130: (1.0000000000000002, 0.7123696111086844),
         140: (1.0, 1.2413505532340796), 150: (1.0, 1.6339745962155616), 160: (1.0, 1.954044648600696),
         170: (1.0, 2.2355095289373024), 180: (5.0, 2.5), 190: (5.0, 2.0591825482288373),
         200: (3.8737387097273115, 2.0), 210: (3.3660254037844384, 2.0), 220: (3.095876796297105, 2.0),
         230: (3.0, 1.9041232037028957), 240: (2.9999999999999996, 1.633974596215563), 250: (3.0, 1.1262612902726907),
         260: (2.9408174517711623, 0.0), 270: (2.5, 5.0), 280: (2.9408174517711614, 5.0), 290: (3.045955351399304, 4.0),
         300: (3.3660254037844384, 4.0), 310: (3.7586494467659204, 4.0), 320: (4.287630388891313, 4.0),
         330: (5.0, 3.9433756729740663), 340: (5.0, 3.409925585665508), 350: (5.0, 2.9408174517711627)},
        {0: (1.0, 2.5), 10: (1.0, 2.9408174517711623), 20: (0.0, 3.7738958199317083), 30: (0.0, 4.52072594216369),
         40: (0.5206160185144741, 5.0), 50: (1.4022509220567994, 5.0), 60: (2.056624327025935, 5.0),
         70: (2.954044648600696, 4.0), 80: (3.235509528937303, 4.0), 90: (3.5, 2.0), 100: (3.4118365096457675, 2.0),
         110: (3.318014882866899, 2.0), 120: (3.211324865405187, 2.0), 130: (3.08045018441136, 2.0),
         140: (1.0, 0.40225092205679935), 150: (1.0, 1.056624327025936), 160: (1.0, 1.5900744143344938),
         170: (1.0, 2.059182548228837), 180: (5.0, 2.5), 190: (5.0, 2.2355095289373024), 200: (5.0, 1.9540446486006964),
         210: (5.0, 1.6339745962155607), 220: (5.0, 1.2413505532340796), 230: (3.9195498155886406, 2.0),
         240: (3.788675134594813, 2.0), 250: (3.681985117133101, 2.0), 260: (3.5881634903542325, 2.0), 270: (3.5, 4.0),
         280: (3.7644904710626967, 4.0), 290: (4.0459553513993045, 4.0), 300: (4.366025403784438, 4.0),
         310: (4.7586494467659195, 4.0), 320: (5.0, 3.7586494467659204), 330: (5.0, 3.3660254037844393),
         340: (5.0, 3.0459553513993045), 350: (5.0, 2.7644904710626976)},
        {0: (1.0, 2.5), 10: (0.0, 3.2934714131880924), 20: (0.0, 4.137866054197911), 30: (0.1698729810778054, 5.0),
         40: (1.5206160185144746, 5.0), 50: (3.24135055323408, 4.0), 60: (3.633974596215561, 4.0),
         70: (3.9540446486006964, 4.0), 80: (4.235509528937302, 4.0), 90: (4.5, 0.0), 100: (4.059182548228837, 0.0),
         110: (4.0, 1.126261290272689), 120: (4.000000000000001, 1.633974596215562), 130: (4.0, 1.9041232037028948),
         140: (3.904123203702895, 2.0), 150: (3.6339745962155607, 2.0), 160: (3.1262612902726903, 2.0),
         170: (1.0, 1.8828555675203718), 180: (5.0, 2.5), 190: (5.0, 2.4118365096457675),
         200: (5.0, 2.3180148828668985), 210: (5.0, 2.211324865405187), 220: (5.0, 2.08045018441136),
         230: (5.0, 1.9041232037028948), 240: (4.999999999999999, 1.633974596215563),
         250: (5.000000000000001, 1.1262612902726912), 260: (4.940817451771163, 0.0), 270: (4.5, 4.0),
         280: (4.764490471062697, 4.0), 290: (5.0, 3.87373870972731), 300: (5.0, 3.366025403784437),
         310: (4.999999999999999, 3.0958767962971048), 320: (5.0, 2.91954981558864), 330: (5.0, 2.788675134594813),
         340: (5.0, 2.681985117133101), 350: (5.0, 2.5881634903542325)},
        {0: (0.0, 3.5), 10: (0.0, 3.5881634903542325), 20: (0.0, 3.681985117133101), 30: (0.0, 3.788675134594813),
         40: (0.0, 3.91954981558864), 50: (9.315877304874933e-17, 4.095876796297105), 60: (-0.0, 4.366025403784438),
         70: (-0.0, 4.873738709727311), 80: (0.23550952893730245, 5.0), 90: (0.5, 3.0), 100: (0.4118365096457675, 3.0),
         110: (0.3180148828668988, 3.0), 120: (0.21132486540518736, 3.0), 130: (0.08045018441136018, 3.0),
         140: (0.0, 3.08045018441136), 150: (0.0, 3.211324865405187), 160: (0.0, 3.3180148828668985),
         170: (0.0, 3.4118365096457675), 180: (5.0, 3.4999999999999996), 190: (5.0, 2.706528586811907),
         200: (5.0, 1.8621339458020896), 210: (3.098076211353315, 2.0), 220: (3.0, 1.4022509220568002),
         230: (0.9195498155886404, 3.0), 240: (0.7886751345948132, 3.0), 250: (0.6819851171331015, 3.0),
         260: (0.5881634903542324, 3.0), 270: (0.5, 5.0), 280: (0.7644904710626967, 5.0), 290: (1.045955351399304, 5.0),
         300: (1.3660254037844386, 5.0), 310: (1.75864944676592, 5.0), 320: (2.287630388891314, 5.0),
         330: (3.0, 4.943375672974066), 340: (3.0, 4.409925585665508), 350: (3.335640909808854, 4.0)},
        {0: (0.0, 3.5), 10: (0.0, 3.7644904710626976), 20: (0.0, 4.045955351399304), 30: (0.0, 4.366025403784438),
         40: (0.0, 4.7586494467659195), 50: (0.24135055323407986, 5.0), 60: (0.6339745962155611, 5.0),
         70: (0.954044648600696, 5.0), 80: (1.2355095289373024, 5.0), 90: (1.5, 0.0), 100: (1.0, 0.6643590901911445),
         110: (1.0, 2.1262612902726885), 120: (0.9999999999999999, 2.6339745962155603),
         130: (1.0000000000000002, 2.9041232037028952), 140: (0.9041232037028951, 3.0), 150: (0.6339745962155611, 3.0),
         160: (0.126261290272689, 3.0), 170: (0.0, 3.235509528937302), 180: (5.0, 3.4999999999999996),
         190: (5.0, 2.882855567520372), 200: (5.0, 2.226104180068292), 210: (5.0, 1.4792740578363088),
         220: (3.287630388891315, 2.0), 230: (3.0, 1.7123696111086861), 240: (3.5207259421636925, 0.0),
         250: (2.7738958199317105, 0.0), 260: (2.1171444324796274, 0.0), 270: (1.5, 5.0), 280: (1.764490471062697, 5.0),
         290: (2.045955351399304, 5.0), 300: (2.366025403784439, 5.0), 310: (2.7586494467659195, 5.0),
         320: (3.0, 4.75864944676592), 330: (3.0, 4.366025403784439), 340: (3.0, 4.045955351399305),
         350: (4.335640909808855, 4.0)},
        {0: (0.0, 3.5), 10: (0.0, 3.9408174517711627), 20: (0.0, 4.409925585665506), 30: (0.0, 4.943375672974064),
         40: (0.7123696111086849, 5.0), 50: (1.2413505532340796, 5.0), 60: (1.6339745962155612, 5.0),
         70: (1.9540446486006964, 5.0), 80: (2.2355095289373024, 5.0), 90: (2.5, 0.0), 100: (1.8828555675203729, 0.0),
         110: (1.2261041800682921, 0.0), 120: (1.0000000000000002, 0.9019237886466831),
         130: (1.0000000000000002, 1.7123696111086844), 140: (1.0, 2.241350553234079), 150: (1.0, 2.6339745962155616),
         160: (1.0, 2.954044648600696), 170: (0.0, 3.0591825482288364), 180: (5.0, 3.5), 190: (5.0, 3.0591825482288373),
         200: (5.0, 2.5900744143344943), 210: (5.0, 2.056624327025935), 220: (5.0, 1.4022509220568002),
         230: (3.758649446765921, 2.0), 240: (3.3660254037844397, 2.0), 250: (3.0459553513993045, 2.0),
         260: (3.117144432479627, 0.0), 270: (2.5, 5.0), 280: (2.7644904710626967, 5.0),
         290: (2.9999999999999996, 4.87373870972731), 300: (2.9999999999999996, 4.366025403784438),
         310: (3.0, 4.095876796297105), 320: (3.0958767962971043, 4.0), 330: (3.3660254037844375, 4.0),
         340: (3.8737387097273075, 4.0), 350: (5.0, 3.9408174517711627)},
        {0: (0.0, 3.5), 10: (0.0, 4.117144432479627), 20: (0.0, 4.773895819931708), 30: (0.9019237886466837, 5.0),
         40: (1.7123696111086844, 5.0), 50: (3.0804501844113594, 4.0), 60: (3.211324865405187, 4.0),
         70: (3.3180148828668985, 4.0), 80: (3.411836509645768, 4.0), 90: (3.5, 2.0), 100: (3.235509528937303, 2.0),
         110: (2.9540446486006964, 2.0), 120: (1.4792740578363108, 0.0), 130: (1.0000000000000002, 0.5206160185144748),
         140: (1.0, 1.4022509220567994), 150: (1.0, 2.056624327025936), 160: (1.0, 2.590074414334494),
         170: (0.6643590901911511, 3.0), 180: (5.0, 3.5), 190: (5.0, 3.2355095289373024),
         200: (5.0, 2.9540446486006964), 210: (5.0, 2.6339745962155607), 220: (5.0, 2.2413505532340796),
         230: (5.0, 1.7123696111086866), 240: (4.999999999999999, 0.9019237886466884), 250: (4.0459553513993045, 2.0),
         260: (3.764490471062697, 2.0), 270: (3.5, 4.0), 280: (3.588163490354232, 4.0), 290: (3.6819851171331015, 4.0),
         300: (3.788675134594813, 4.0), 310: (3.9195498155886397, 4.0), 320: (4.095876796297105, 4.0),
         330: (4.3660254037844375, 4.0), 340: (4.873738709727308, 4.0), 350: (5.0, 3.7644904710626976)},
        {0: (0.0, 3.5), 10: (0.0, 4.293471413188092), 20: (3.1262612902726885, 4.0), 30: (3.6339745962155607, 4.0),
         40: (3.9041232037028952, 4.0), 50: (4.08045018441136, 4.0), 60: (4.211324865405187, 4.0),
         70: (4.3180148828668985, 4.0), 80: (4.4118365096457675, 4.0), 90: (4.5, 0.0), 100: (3.8828555675203726, 0.0),
         110: (3.9540446486006964, 2.0), 120: (3.6339745962155616, 2.0), 130: (3.2413505532340805, 2.0),
         140: (1.0, 0.5631512908795191), 150: (1.0, 1.4792740578363106), 160: (1.0, 2.226104180068291),
         170: (1.0, 2.8828555675203718), 180: (5.0, 3.5), 190: (5.0, 3.4118365096457675),
         200: (5.0, 3.3180148828668985), 210: (5.0, 3.211324865405187), 220: (5.0, 3.08045018441136),
         230: (5.0, 2.9041232037028952), 240: (4.999999999999999, 2.6339745962155634),
         250: (5.000000000000001, 2.126261290272691), 260: (5.0, 0.6643590901911436), 270: (4.5, 4.0),
         280: (4.5881634903542325, 4.0), 290: (4.6819851171331015, 4.0), 300: (4.788675134594813, 4.0),
         310: (4.91954981558864, 4.0), 320: (5.0, 3.91954981558864), 330: (5.0, 3.788675134594813),
         340: (5.0, 3.6819851171331015), 350: (5.0, 3.5881634903542325)},
        {0: (0.0, 4.5), 10: (0.0, 4.5881634903542325), 20: (0.0, 4.6819851171331015), 30: (0.0, 4.788675134594813),
         40: (0.0, 4.91954981558864), 50: (0.08045018441135993, 5.0), 60: (0.21132486540518702, 5.0),
         70: (0.3180148828668988, 5.0), 80: (0.41183650964576746, 5.0), 90: (0.5, 3.0), 100: (0.23550952893730262, 3.0),
         110: (0.0, 3.126261290272689), 120: (0.0, 3.6339745962155607), 130: (0.0, 3.904123203702895),
         140: (0.0, 4.08045018441136), 150: (0.0, 4.211324865405187), 160: (0.0, 4.3180148828668985),
         170: (0.0, 4.4118365096457675), 180: (3.0, 4.5), 190: (3.0, 4.059182548228837), 200: (5.0, 2.8621339458020896),
         210: (5.0, 1.901923788646683), 220: (3.479383981485526, 2.0), 230: (3.0, 1.520616018514477),
         240: (3.098076211353319, 0.0), 250: (1.0459553513993045, 3.0), 260: (0.7644904710626975, 3.0), 270: (0.5, 5.0),
         280: (0.5881634903542323, 5.0), 290: (0.6819851171331014, 5.0), 300: (0.7886751345948129, 5.0),
         310: (0.91954981558864, 5.0), 320: (1.0958767962971045, 5.0), 330: (1.3660254037844377, 5.0),
         340: (1.8737387097273082, 5.0), 350: (3.0, 4.940817451771163)},
        {0: (0.0, 4.5), 10: (0.0, 4.764490471062698), 20: (0.1262612902726888, 5.0), 30: (0.6339745962155611, 5.0),
         40: (0.9041232037028949, 5.0), 50: (1.08045018441136, 5.0), 60: (1.2113248654051871, 5.0),
         70: (1.3180148828668985, 5.0), 80: (1.4118365096457675, 5.0), 90: (1.5, 0.0),
         100: (1.0000000000000002, 1.6643590901911454), 110: (0.9540446486006966, 3.0), 120: (0.6339745962155618, 3.0),
         130: (0.24135055323408017, 3.0), 140: (0.0, 3.2413505532340796), 150: (0.0, 3.6339745962155616),
         160: (0.0, 3.9540446486006964), 170: (0.0, 4.2355095289373015), 180: (3.0, 4.5), 190: (3.0, 4.235509528937302),
         200: (3.0, 3.9540446486006964), 210: (5.0, 2.479274057836309), 220: (5.0, 1.56315129087952),
         230: (3.597749077943201, 2.0), 240: (2.9999999999999996, 1.9019237886466875), 250: (3.1378660541979135, 0.0),
         260: (2.293471413188092, 0.0), 270: (1.5, 5.0), 280: (1.5881634903542323, 5.0), 290: (1.6819851171331015, 5.0),
         300: (1.788675134594813, 5.0), 310: (1.91954981558864, 5.0), 320: (2.0958767962971048, 5.0),
         330: (2.3660254037844375, 5.0), 340: (2.8737387097273084, 5.0), 350: (3.0, 4.764490471062698)},
        {0: (0.0, 4.5), 10: (0.0, 4.940817451771163), 20: (1.1262612902726887, 5.0), 30: (1.6339745962155612, 5.0),
         40: (1.9041232037028952, 5.0), 50: (2.08045018441136, 5.0), 60: (2.211324865405187, 5.0),
         70: (2.318014882866899, 5.0), 80: (2.4118365096457675, 5.0), 90: (2.5, 0.0), 100: (1.7065285868119078, 0.0),
         110: (1.0000000000000002, 0.37878387081806686), 120: (1.0000000000000002, 1.901923788646683),
         130: (0.9999999999999998, 2.7123696111086844), 140: (0.712369611108686, 3.0), 150: (0.0, 3.056624327025936),
         160: (0.0, 3.5900744143344934), 170: (0.0, 4.059182548228836), 180: (3.0, 4.5), 190: (3.0, 4.4118365096457675),
         200: (3.0, 4.318014882866899), 210: (3.0, 4.211324865405187), 220: (3.0, 4.08045018441136),
         230: (5.0, 1.520616018514477), 240: (3.9433756729740663, 2.0), 250: (3.4099255856655075, 2.0),
         260: (3.0000000000000004, 1.6643590901911445), 270: (2.5, 5.0), 280: (2.588163490354232, 5.0),
         290: (2.681985117133101, 5.0), 300: (2.7886751345948126, 5.0), 310: (2.91954981558864, 5.0),
         320: (3.0, 4.91954981558864), 330: (3.0, 4.788675134594813), 340: (3.0, 4.6819851171331015),
         350: (3.0, 4.5881634903542325)}]
    alpha_diff = 10
    for position, correct_scan in zip(positions, correct_scans):
        x, y, _ = position
        scan = generate(x, y, local_map, alpha_diff)
        assert scan == correct_scan
