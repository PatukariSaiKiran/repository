products_list = {
        1: {
            "name": "Laptop",
            "img": "laptop_img.jpg",
            "title": "The new MacBook Pro is available in 35.97-centimetre (14.2-inch) and 41.05-centimetre (16.2-inch) models."
        },
        2: {
            "name": "Television",
            "img": "tv_img.jpg",
            "title": "Sony TV 80cm (32 Inch) HD Ready LED Smart TV (3 Years Warranty, Alexa Voice Assistant Remote, CREL7364, Black)"
        },
        3: {
            "name": "VR Headset",
            "img": "vr_img.jpg",
            "title": "VR Headset Compatible with iPhone & Android Phone - Universal Virtual Reality Goggles - Soft & Comfortable New 3D VR Glasses (Blue)"
        },
        
        4: {
            "name": "Airpods",
            "img": "iphone Airpods_img.jpg",
            "title": "AirPods (3rd generation)"
        },
        5: {
            "name": "alexa dot_img",
            "img": "alexa dot_img.jpg",
            "title": "Echo Dot (3rd Gen) New and improved smart speaker with Alexa (Black)"
        },
        6: {
            "name": "moblie",
            "img": "IPHONE_img.jpg",
            "title": "Apple iPhone 13 Pro (128 GB)  Alpine Green"
        }
    }
  
empty_cart={}
for key,value in products_list.items():
    empty_cart[key]={
        'name':value['name']
        ,
        'quantity':0
    }
