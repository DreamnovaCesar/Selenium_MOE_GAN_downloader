
"""
Attributes
----------
_ID_QUERY_ : str
    The ID value of the HTML element containing the search query.
_ID_SEARCH_ : str
    The ID value of the HTML element containing the search results.
_CONTENT_LIST_ : str
    The class name of the HTML element containing the search results list.
_TAG_NAME_LI_ : str
    The tag name of the HTML element representing each search result item.
_BIBLIOGRAPHIC_INFO_LIST_ : str
    The class name of the HTML element containing bibliographic information for a search result.
_BIBLIOGRAPHIC_INFO_VALUE_ : str
    The class name of the HTML element containing the value of a bibliographic information item.
_DOI_TEXT_ : str
    The text identifier used for the Digital Object Identifier in bibliographic information.
_BIBLIOGRAPHIC_INFO_LIST_UMB24_ : str
    The class name of the HTML element containing additional bibliographic information for a search result.
_DIGITAL_OBJECT_IDENTIFIER_ : str
    The full text identifier used for the Digital Object Identifier in bibliographic information.
_NEXT_CONTEST_LIST_ : str
    The value representing the "Next" button in a list of search results.

"""

_XPATH_MODEL_BUTTON_ = '//*[@id="root"]/div/div/div/div/div[1]/div[2]/div[2]/div/div[2]/div/div/button'
_XPATH_MODEL_OPEN_ = '//*[@id="root"]/div/div/div/div/div[1]/div[2]/div[2]/div/div[2]/div/div/ul'

_XPATH_HAIR_COLOR_BUTTON_ = '//*[@id="root"]/div/div/div/div/div[1]/div[2]/div[2]/div/div[3]/div[1]/div/button'
_XPATH_HAIR_COLOR_OPEN_ = '//*[@id="root"]/div/div/div/div/div[1]/div[2]/div[2]/div/div[3]/div[1]/div/ul'

_XPATH_HAIR_STYLE_BUTTON_ = '//*[@id="root"]/div/div/div/div/div[1]/div[2]/div[2]/div/div[3]/div[2]/div/button'
_XPATH_HAIR_STYLE_OPEN_ = '//*[@id="root"]/div/div/div/div/div[1]/div[2]/div[2]/div/div[3]/div[2]/div/ul'

_XPATH_EYE_COLOR_BUTTON_ = '//*[@id="root"]/div/div/div/div/div[1]/div[2]/div[2]/div/div[3]/div[3]/div/button'
_XPATH_EYE_COLOR_OPEN_ = '//*[@id="root"]/div/div/div/div/div[1]/div[2]/div[2]/div/div[3]/div[3]/div/ul'

_XPATH_DARK_SKIN_OFF_BUTTON_ = '//*[@id="root"]/div/div/div/div/div[1]/div[2]/div[2]/div/div[3]/div[4]/div/button[1]'
_XPATH_DARK_SKIN_RANDOM_BUTTON_ = '//*[@id="root"]/div/div/div/div/div[1]/div[2]/div[2]/div/div[3]/div[4]/div/button[2]'
_XPATH_DARK_SKIN_ON_BUTTON_ = '//*[@id="root"]/div/div/div/div/div[1]/div[2]/div[2]/div/div[3]/div[4]/div/button[3]'

_XPATH_BLUSH_OFF_BUTTON_ = '//*[@id="root"]/div/div/div/div/div[1]/div[2]/div[2]/div/div[3]/div[5]/div/button[1]'
_XPATH_BLUSH_RANDOM_BUTTON_ = '//*[@id="root"]/div/div/div/div/div[1]/div[2]/div[2]/div/div[3]/div[5]/div/button[2]'
_XPATH_BLUSH_ON_BUTTON_ = '//*[@id="root"]/div/div/div/div/div[1]/div[2]/div[2]/div/div[3]/div[5]/div/button[3]'

_XPATH_SMILE_OFF_BUTTON_ = '//*[@id="root"]/div/div/div/div/div[1]/div[2]/div[2]/div/div[3]/div[6]/div/button[1]'
_XPATH_SMILE_RANDOM_BUTTON_ = '//*[@id="root"]/div/div/div/div/div[1]/div[2]/div[2]/div/div[3]/div[6]/div/button[2]'
_XPATH_SMILE_ON_BUTTON_ = '//*[@id="root"]/div/div/div/div/div[1]/div[2]/div[2]/div/div[3]/div[6]/div/button[3]'

_XPATH_OPEN_MOUTH_OFF_BUTTON_ = '//*[@id="root"]/div/div/div/div/div[1]/div[2]/div[2]/div/div[3]/div[7]/div/button[1]'
_XPATH_OPEN_MOUTH_RANDOM_BUTTON_ = '//*[@id="root"]/div/div/div/div/div[1]/div[2]/div[2]/div/div[3]/div[7]/div/button[2]'
_XPATH_OPEN_MOUTH_ON_BUTTON_ = '//*[@id="root"]/div/div/div/div/div[1]/div[2]/div[2]/div/div[3]/div[7]/div/button[3]'

_XPATH_HAT_OFF_BUTTON_ = '//*[@id="root"]/div/div/div/div/div[1]/div[2]/div[2]/div/div[3]/div[8]/div/button[1]'
_XPATH_HAT_RANDOM_BUTTON_ = '//*[@id="root"]/div/div/div/div/div[1]/div[2]/div[2]/div/div[3]/div[8]/div/button[2]'
_XPATH_HAT_ON_BUTTON_ = '//*[@id="root"]/div/div/div/div/div[1]/div[2]/div[2]/div/div[3]/div[8]/div/button[3]'

_XPATH_RIBBON_OFF_BUTTON_ = '//*[@id="root"]/div/div/div/div/div[1]/div[2]/div[2]/div/div[3]/div[9]/div/button[1]'
_XPATH_RIBBON_RANDOM_BUTTON_ = '//*[@id="root"]/div/div/div/div/div[1]/div[2]/div[2]/div/div[3]/div[9]/div/button[2]'
_XPATH_RIBBON_ON_BUTTON_ = '//*[@id="root"]/div/div/div/div/div[1]/div[2]/div[2]/div/div[3]/div[9]/div/button[3]'

_XPATH_GLASSES_OFF_BUTTON_ = '//*[@id="root"]/div/div/div/div/div[1]/div[2]/div[2]/div/div[3]/div[10]/div/button[1]'
_XPATH_GLASSES_RANDOM_BUTTON_ = '//*[@id="root"]/div/div/div/div/div[1]/div[2]/div[2]/div/div[3]/div[10]/div/button[2]'
_XPATH_GLASSES_ON_BUTTON_ = '//*[@id="root"]/div/div/div/div/div[1]/div[2]/div[2]/div/div[3]/div[10]/div/button[3]'

_XPATH_IMAGE_ = '//*[@id="root"]/div/div/div/div/div[1]/div[2]/div[1]/div/div[1]/div/div/img'
_XPATH_BUTTON_ = '//*[@id="root"]/div/div/div/div/div[1]/div[2]/div[1]/div/button'

