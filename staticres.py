shiyongurl = "http://m.isms360.com/customize/ProcessShiyong.ashx"
imgurl = "http://m.isms360.com/inc/verificationcode.aspx"
comstr = "0123456789abcdefghijklmnopqrstuvwxyz"
header = {"Origin": "http://m.isms360.com", "X-Requested-With": "XMLHttpRequest",
          "Referer": "http://m.isms360.com/channel.aspx?id=21",
          "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
          "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"}
regionlist = [
    {
        "Id": 1,
        "CountryCh": "美国",
        "CountryEn": "U.S.A",
        "CountryCode": "1"
    },
    {
        "Id": 2,
        "CountryCh": "加拿大",
        "CountryEn": "Canada",
        "CountryCode": "1"
    },
    {
        "Id": 3,
        "CountryCh": "中国",
        "CountryEn": "China",
        "CountryCode": "86"
    },
    {
        "Id": 4,
        "CountryCh": "香港",
        "CountryEn": "Hongkong",
        "CountryCode": "852"
    },
    {
        "Id": 5,
        "CountryCh": "澳门",
        "CountryEn": "Macao",
        "CountryCode": "853"
    },
    {
        "Id": 6,
        "CountryCh": "台湾",
        "CountryEn": "Taiwan",
        "CountryCode": "886"
    },
    {
        "Id": 7,
        "CountryCh": "日本",
        "CountryEn": "Japan",
        "CountryCode": "81"
    },
    {
        "Id": 8,
        "CountryCh": "韩国",
        "CountryEn": "Korea",
        "CountryCode": "82"
    },
    {
        "Id": 9,
        "CountryCh": "马来西亚",
        "CountryEn": "Malaysia",
        "CountryCode": "60"
    },
    {
        "Id": 10,
        "CountryCh": "新加坡",
        "CountryEn": "Singapore",
        "CountryCode": "65"
    },
    {
        "Id": 11,
        "CountryCh": "泰国",
        "CountryEn": "Thailand",
        "CountryCode": "66"
    },
    {
        "Id": 12,
        "CountryCh": "菲律宾",
        "CountryEn": "Philippines",
        "CountryCode": "63"
    },
    {
        "Id": 13,
        "CountryCh": "印度尼西亚",
        "CountryEn": "Indonesia",
        "CountryCode": "62"
    },
    {
        "Id": 14,
        "CountryCh": "柬埔寨",
        "CountryEn": "Cambodia",
        "CountryCode": "855"
    },
    {
        "Id": 15,
        "CountryCh": "汶莱",
        "CountryEn": "Brunei Darussalam",
        "CountryCode": "673"
    },
    {
        "Id": 16,
        "CountryCh": "斯里兰卡",
        "CountryEn": "SRILANKA",
        "CountryCode": "94"
    },
    {
        "Id": 17,
        "CountryCh": "蒙古",
        "CountryEn": "Mongolia",
        "CountryCode": "976"
    },
    {
        "Id": 18,
        "CountryCh": "老挝",
        "CountryEn": "Laos",
        "CountryCode": "856"
    },
    {
        "Id": 19,
        "CountryCh": "帕劳",
        "CountryEn": "Palau",
        "CountryCode": "680"
    },
    {
        "Id": 20,
        "CountryCh": "所罗门群岛",
        "CountryEn": "Solomon Islands",
        "CountryCode": "677"
    },
    {
        "Id": 21,
        "CountryCh": "缅甸",
        "CountryEn": "MYANMAR",
        "CountryCode": "509"
    },
    {
        "Id": 22,
        "CountryCh": "越南",
        "CountryEn": "Vietnam",
        "CountryCode": "84"
    },
    {
        "Id": 23,
        "CountryCh": "巴基斯坦",
        "CountryEn": "Pakistan",
        "CountryCode": "92"
    },
    {
        "Id": 24,
        "CountryCh": "印度",
        "CountryEn": "India",
        "CountryCode": "91"
    },
    {
        "Id": 25,
        "CountryCh": "孟加拉",
        "CountryEn": "Bangladesh",
        "CountryCode": "880"
    },
    {
        "Id": 26,
        "CountryCh": "阿富汗",
        "CountryEn": "Afghanistan",
        "CountryCode": "93"
    },
    {
        "Id": 27,
        "CountryCh": "尼泊尔",
        "CountryEn": "Nepal",
        "CountryCode": "977"
    },
    {
        "Id": 28,
        "CountryCh": "吉尔吉斯斯坦",
        "CountryEn": "Kyrgyz Public",
        "CountryCode": "996"
    },
    {
        "Id": 29,
        "CountryCh": "塔吉克斯坦",
        "CountryEn": "Tajikistan",
        "CountryCode": "992"
    },
    {
        "Id": 30,
        "CountryCh": "土库曼斯坦",
        "CountryEn": "Turkmenistan",
        "CountryCode": "993"
    },
    {
        "Id": 31,
        "CountryCh": "乌兹别克斯坦",
        "CountryEn": "Uzbekistan",
        "CountryCode": "998"
    },
    {
        "Id": 32,
        "CountryCh": "阿塞拜疆",
        "CountryEn": "Azerbaijan",
        "CountryCode": "994"
    },
    {
        "Id": 33,
        "CountryCh": "迪拜",
        "CountryEn": "Dubai",
        "CountryCode": "971"
    },
    {
        "Id": 34,
        "CountryCh": "沙特阿拉伯",
        "CountryEn": "Saudi Arabia",
        "CountryCode": "966"
    },
    {
        "Id": 35,
        "CountryCh": "阿联酋",
        "CountryEn": "U.A.E",
        "CountryCode": "971"
    },
    {
        "Id": 36,
        "CountryCh": "叙利亚",
        "CountryEn": "Syria",
        "CountryCode": "963"
    },
    {
        "Id": 37,
        "CountryCh": "卡塔尔",
        "CountryEn": "Qatar",
        "CountryCode": "974"
    },
    {
        "Id": 38,
        "CountryCh": "科威特",
        "CountryEn": "Kuwait",
        "CountryCode": "965"
    },
    {
        "Id": 39,
        "CountryCh": "伊朗",
        "CountryEn": "Iran",
        "CountryCode": "98"
    },
    {
        "Id": 40,
        "CountryCh": "伊拉克",
        "CountryEn": "Iraq",
        "CountryCode": "964"
    },
    {
        "Id": 41,
        "CountryCh": "约旦",
        "CountryEn": "Jordan",
        "CountryCode": "962"
    },
    {
        "Id": 42,
        "CountryCh": "巴勒斯坦",
        "CountryEn": "Palestine",
        "CountryCode": "970"
    },
    {
        "Id": 43,
        "CountryCh": "以色列",
        "CountryEn": "Israel",
        "CountryCode": "972"
    },
    {
        "Id": 44,
        "CountryCh": "澳大利亚",
        "CountryEn": "Australia",
        "CountryCode": "61"
    },
    {
        "Id": 45,
        "CountryCh": "新西兰",
        "CountryEn": "New Zealand",
        "CountryCode": "64"
    },
    {
        "Id": 46,
        "CountryCh": "英国",
        "CountryEn": "United Kiongdom",
        "CountryCode": "44"
    },
    {
        "Id": 47,
        "CountryCh": "法国",
        "CountryEn": "France",
        "CountryCode": "33"
    },
    {
        "Id": 48,
        "CountryCh": "德国",
        "CountryEn": "Germany",
        "CountryCode": "49"
    },
    {
        "Id": 49,
        "CountryCh": "西班牙",
        "CountryEn": "Spain",
        "CountryCode": "34"
    },
    {
        "Id": 50,
        "CountryCh": "瑞典",
        "CountryEn": "Sweden",
        "CountryCode": "46"
    },
    {
        "Id": 51,
        "CountryCh": "瑞士",
        "CountryEn": "Switzerland",
        "CountryCode": "41"
    },
    {
        "Id": 52,
        "CountryCh": "意大利",
        "CountryEn": "Italy",
        "CountryCode": "39"
    },
    {
        "Id": 53,
        "CountryCh": "奥地利",
        "CountryEn": "Austria",
        "CountryCode": "43"
    },
    {
        "Id": 54,
        "CountryCh": "比利时",
        "CountryEn": "Belgium",
        "CountryCode": "32"
    },
    {
        "Id": 55,
        "CountryCh": "丹麦",
        "CountryEn": "Denmark",
        "CountryCode": "45"
    },
    {
        "Id": 56,
        "CountryCh": "芬兰",
        "CountryEn": "Finland",
        "CountryCode": "358"
    },
    {
        "Id": 57,
        "CountryCh": "荷兰",
        "CountryEn": "Netherlands",
        "CountryCode": "31"
    },
    {
        "Id": 58,
        "CountryCh": "挪威",
        "CountryEn": "Norway",
        "CountryCode": "47"
    },
    {
        "Id": 59,
        "CountryCh": "匈牙利",
        "CountryEn": "Hungray",
        "CountryCode": "36"
    },
    {
        "Id": 60,
        "CountryCh": "罗马尼亚",
        "CountryEn": "Romania",
        "CountryCode": "40"
    },
    {
        "Id": 61,
        "CountryCh": "波兰",
        "CountryEn": "Poland",
        "CountryCode": "48"
    },
    {
        "Id": 62,
        "CountryCh": "乌克兰",
        "CountryEn": "Ukraine",
        "CountryCode": "380"
    },
    {
        "Id": 63,
        "CountryCh": "希腊",
        "CountryEn": "Greece",
        "CountryCode": "30"
    },
    {
        "Id": 64,
        "CountryCh": "俄罗斯",
        "CountryEn": "Russia",
        "CountryCode": "7"
    },
    {
        "Id": 65,
        "CountryCh": "土耳其",
        "CountryEn": "Turky",
        "CountryCode": "90"
    },
    {
        "Id": 66,
        "CountryCh": "捷克",
        "CountryEn": "Czech Republic",
        "CountryCode": "420"
    },
    {
        "Id": 67,
        "CountryCh": "保加利亚",
        "CountryEn": "Bulgaria",
        "CountryCode": "359"
    },
    {
        "Id": 68,
        "CountryCh": "克罗地亚",
        "CountryEn": "Croatia",
        "CountryCode": "385"
    },
    {
        "Id": 69,
        "CountryCh": "塞浦路斯",
        "CountryEn": "Cyprus",
        "CountryCode": "357"
    },
    {
        "Id": 70,
        "CountryCh": "爱尔兰",
        "CountryEn": "Ireland",
        "CountryCode": "353"
    },
    {
        "Id": 71,
        "CountryCh": "希腊",
        "CountryEn": "Greece",
        "CountryCode": "30"
    },
    {
        "Id": 72,
        "CountryCh": "立陶宛",
        "CountryEn": "Lithuania",
        "CountryCode": "370"
    },
    {
        "Id": 73,
        "CountryCh": "卢森堡",
        "CountryEn": "Luxembourg",
        "CountryCode": "352"
    },
    {
        "Id": 74,
        "CountryCh": "摩洛哥",
        "CountryEn": "Morocco",
        "CountryCode": "212"
    },
    {
        "Id": 75,
        "CountryCh": "葡萄牙",
        "CountryEn": "Portugal",
        "CountryCode": "351"
    },
    {
        "Id": 76,
        "CountryCh": "摩纳哥",
        "CountryEn": "Monaco",
        "CountryCode": "377"
    },
    {
        "Id": 77,
        "CountryCh": "塞尔维亚",
        "CountryEn": "Serbia",
        "CountryCode": "381"
    },
    {
        "Id": 78,
        "CountryCh": "斯洛伐克",
        "CountryEn": "Slovakia",
        "CountryCode": "421"
    },
    {
        "Id": 79,
        "CountryCh": "拉脱维亚",
        "CountryEn": "Latvia",
        "CountryCode": "371"
    },
    {
        "Id": 80,
        "CountryCh": "斯洛文尼亚",
        "CountryEn": "SLOVENIA",
        "CountryCode": "368"
    },
    {
        "Id": 81,
        "CountryCh": "安道尔",
        "CountryEn": "Andorra",
        "CountryCode": "376"
    },
    {
        "Id": 82,
        "CountryCh": "阿尔及利亚",
        "CountryEn": "Algeria",
        "CountryCode": "213"
    },
    {
        "Id": 83,
        "CountryCh": "白俄罗斯",
        "CountryEn": "Belarus",
        "CountryCode": "375"
    },
    {
        "Id": 84,
        "CountryCh": "哈萨克斯坦",
        "CountryEn": "Kazakhstan",
        "CountryCode": "7"
    },
    {
        "Id": 85,
        "CountryCh": "直布罗陀",
        "CountryEn": "Gibraltar",
        "CountryCode": "350"
    },
    {
        "Id": 86,
        "CountryCh": "巴西",
        "CountryEn": "Brazil",
        "CountryCode": "55"
    },
    {
        "Id": 87,
        "CountryCh": "墨西哥",
        "CountryEn": "Mexico",
        "CountryCode": "52"
    },
    {
        "Id": 88,
        "CountryCh": "多米尼加共和国",
        "CountryEn": "Dominican Republic",
        "CountryCode": "1890"
    },
    {
        "Id": 89,
        "CountryCh": "厄瓜多尔",
        "CountryEn": "Ecuador",
        "CountryCode": "593"
    },
    {
        "Id": 90,
        "CountryCh": "智利",
        "CountryEn": "Chile",
        "CountryCode": "56"
    },
    {
        "Id": 91,
        "CountryCh": "哥伦比亚",
        "CountryEn": "Colombia",
        "CountryCode": "57"
    },
    {
        "Id": 92,
        "CountryCh": "秘鲁",
        "CountryEn": "PERU",
        "CountryCode": "51"
    },
    {
        "Id": 93,
        "CountryCh": "古巴",
        "CountryEn": "Cuba",
        "CountryCode": "53"
    },
    {
        "Id": 94,
        "CountryCh": "阿根廷",
        "CountryEn": "Argentina",
        "CountryCode": "54"
    },
    {
        "Id": 95,
        "CountryCh": "委内瑞拉",
        "CountryEn": "Venezuela",
        "CountryCode": "58"
    },
    {
        "Id": 96,
        "CountryCh": "巴哈马",
        "CountryEn": "Bahamas",
        "CountryCode": "1242"
    },
    {
        "Id": 97,
        "CountryCh": "巴林",
        "CountryEn": "Bahrain",
        "CountryCode": "973"
    },
    {
        "Id": 98,
        "CountryCh": "危地马拉",
        "CountryEn": "Guatemala",
        "CountryCode": "502"
    },
    {
        "Id": 99,
        "CountryCh": "洪都拉斯",
        "CountryEn": "Honduras",
        "CountryCode": "504"
    },
    {
        "Id": 100,
        "CountryCh": "荷属安的列斯",
        "CountryEn": "Netherlands Antilles",
        "CountryCode": "599"
    },
    {
        "Id": 101,
        "CountryCh": "尼加拉瓜",
        "CountryEn": "Nicaragua",
        "CountryCode": "505"
    },
    {
        "Id": 102,
        "CountryCh": "巴拿马",
        "CountryEn": "Panama",
        "CountryCode": "507"
    },
    {
        "Id": 103,
        "CountryCh": "巴布亚新几内亚",
        "CountryEn": "Papua New Guinea",
        "CountryCode": "675"
    },
    {
        "Id": 104,
        "CountryCh": "巴拉圭",
        "CountryEn": "Paraguay",
        "CountryCode": "595"
    },
    {
        "Id": 105,
        "CountryCh": "玻利维亚",
        "CountryEn": "Bolivia",
        "CountryCode": "591"
    },
    {
        "Id": 106,
        "CountryCh": "乌拉圭",
        "CountryEn": "Uruguay",
        "CountryCode": "598"
    },
    {
        "Id": 107,
        "CountryCh": "萨尔瓦多",
        "CountryEn": "El Salvador",
        "CountryCode": "503"
    },
    {
        "Id": 108,
        "CountryCh": "哥斯达黎加",
        "CountryEn": "Costa Rica",
        "CountryCode": "506"
    },
    {
        "Id": 109,
        "CountryCh": "南非",
        "CountryEn": "South Africa",
        "CountryCode": "27"
    },
    {
        "Id": 110,
        "CountryCh": "埃及",
        "CountryEn": "Egypt",
        "CountryCode": "20"
    },
    {
        "Id": 111,
        "CountryCh": "坦桑尼亚",
        "CountryEn": "Tanzania",
        "CountryCode": "255"
    },
    {
        "Id": 112,
        "CountryCh": "苏丹",
        "CountryEn": "Sudan",
        "CountryCode": "249"
    },
    {
        "Id": 113,
        "CountryCh": "赞比亚",
        "CountryEn": "Zambia",
        "CountryCode": "260"
    },
    {
        "Id": 114,
        "CountryCh": "尼日尔",
        "CountryEn": "Nigeria",
        "CountryCode": "227"
    },
    {
        "Id": 115,
        "CountryCh": "肯尼亚",
        "CountryEn": "Kenya",
        "CountryCode": "254"
    },
    {
        "Id": 116,
        "CountryCh": "诶塞俄比亚",
        "CountryEn": "Ethiopia",
        "CountryCode": "251"
    },
    {
        "Id": 117,
        "CountryCh": "喀麦隆",
        "CountryEn": "Cameroon",
        "CountryCode": "237"
    },
    {
        "Id": 118,
        "CountryCh": "安哥拉",
        "CountryEn": "Angola",
        "CountryCode": "244"
    },
    {
        "Id": 119,
        "CountryCh": "乌干达",
        "CountryEn": "Uganda",
        "CountryCode": "256"
    },
    {
        "Id": 120,
        "CountryCh": "刚果",
        "CountryEn": "Congo",
        "CountryCode": "242"
    },
    {
        "Id": 121,
        "CountryCh": "刚果金",
        "CountryEn": "Congo Rep",
        "CountryCode": "243"
    },
    {
        "Id": 122,
        "CountryCh": "苏丹",
        "CountryEn": "Sudan",
        "CountryCode": "249"
    },
    {
        "Id": 123,
        "CountryCh": "坦桑尼亚",
        "CountryEn": "Tanzania",
        "CountryCode": "255"
    },
    {
        "Id": 124,
        "CountryCh": "博茨瓦纳",
        "CountryEn": "Botswana",
        "CountryCode": "267"
    },
    {
        "Id": 125,
        "CountryCh": "马拉维",
        "CountryEn": "Malawi",
        "CountryCode": "265"
    },
    {
        "Id": 126,
        "CountryCh": "莫桑比克",
        "CountryEn": "Mozambique",
        "CountryCode": "258"
    },
    {
        "Id": 127,
        "CountryCh": "加纳",
        "CountryEn": "Ghana",
        "CountryCode": "233"
    },
    {
        "Id": 128,
        "CountryCh": "尼日利亚",
        "CountryEn": "Nigeria",
        "CountryCode": "234"
    },
    {
        "Id": 129,
        "CountryCh": "毛里求斯",
        "CountryEn": "Mauritius",
        "CountryCode": "230"
    },
    {
        "Id": 130,
        "CountryCh": "卢旺达",
        "CountryEn": "Rwanda",
        "CountryCode": "250"
    },
    {
        "Id": 131,
        "CountryCh": "塞内加尔",
        "CountryEn": "Senegal",
        "CountryCode": "221"
    },
    {
        "Id": 132,
        "CountryCh": "塞拉利昂",
        "CountryEn": "Sierra Leone",
        "CountryCode": "232"
    },
    {
        "Id": 133,
        "CountryCh": "赞比亚",
        "CountryEn": "Zambia",
        "CountryCode": "260"
    },
    {
        "Id": 134,
        "CountryCh": "津巴布韦",
        "CountryEn": "Zimbabwe",
        "CountryCode": "263"
    },
    {
        "Id": 135,
        "CountryCh": "也门",
        "CountryEn": "Yemen",
        "CountryCode": "967"
    },
    {
        "Id": 136,
        "CountryCh": "乌干达",
        "CountryEn": "Uganda",
        "CountryCode": "256"
    },
    {
        "Id": 137,
        "CountryCh": "贝宁",
        "CountryEn": "Benin",
        "CountryCode": "229"
    },
    {
        "Id": 138,
        "CountryCh": "中非共和国",
        "CountryEn": "Central African Republic",
        "CountryCode": "236"
    },
    {
        "Id": 139,
        "CountryCh": "科特迪瓦",
        "CountryEn": "Ivory Coast",
        "CountryCode": "225"
    },
    {
        "Id": 140,
        "CountryCh": "马达加斯加",
        "CountryEn": "Madagascar",
        "CountryCode": "261"
    },
    {
        "Id": 141,
        "CountryCh": "马里",
        "CountryEn": "Mali",
        "CountryCode": "223"
    },
    {
        "Id": 142,
        "CountryCh": "斐济",
        "CountryEn": "Fiji",
        "CountryCode": "679"
    },
    {
        "Id": 143,
        "CountryCh": "吉布提",
        "CountryEn": "DJIBOUTI",
        "CountryCode": "253"
    },
    {
        "Id": 144,
        "CountryCh": "纳米比亚",
        "CountryEn": "Namibia",
        "CountryCode": "264"
    },
    {
        "Id": 145,
        "CountryCh": "海地",
        "CountryEn": "Haiti",
        "CountryCode": "509"
    }
]
