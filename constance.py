#!/usr/bin/python 
# -*- coding: utf-8 -*-
'''
Created on 20191012

@author: shun
'''
MAVEN_CMD = "mvn install:install-file -DgroupId=%s -DartifactId=%s -Dversion=%s -Dpackaging=aar -Dfile=%s"

GROUP_ID_TAURUSX = "com.taurusx.ads"
GROUP_ID_ADLIME = "com.access_company.adlime"
GROUP_ID_WESDK = "com.we.sdk"

# AAR_INFO = {
#     "duadplatform_cw-1.2.2.aar":{"version":"1.2.2", "artifactId":"duadplatform_cw"},
#     "duadplatform_hw-1.2.2.aar":{"version":"1.2.2", "artifactId":"duadplatform_hw"},
#     "ia-mraid-kit-release-7.2.1.aar":{"version":"7.2.1", "artifactId":"ia-mraid-kit-release"},
#     "ia-native-kit-release-7.2.1.aar":{"version":"7.2.1", "artifactId":"ia-native-kit-release"},
#     "ia-sdk-core-release-7.2.1.aar":{"version":"7.2.1", "artifactId":"ia-sdk-core-release"},
#     "ia-video-kit-release-7.2.1.aar":{"version":"7.2.1", "artifactId":"ia-video-kit-release"},
#     "mopub-moat-mobile-app-kit-2.4.5.aar":{"version":"2.4.5", "artifactId":"mopub-moat-mobile-app-kit"},
#     "mopub-sdk-interstitial-5.7.1.aar":{"version":"5.7.1", "artifactId":"mopub-sdk-interstitial"},
#     "toutiao_open_ad_sdk-2.3.0.7.aar":{"version":"2.3.0.7", "artifactId":"toutiao_open_ad_sdk"},
#     "criteopublishersdk-3.0.1.aar":{"version":"3.0.1", "artifactId":"criteopublishersdk"},
#     "unity-ads-3.1.0.aar":{"version":"3.1.0", "artifactId":"unity-ads"}
# }
AAR_INFO = {
    "bidding-kit-sdk-5.0.1.aar":{"version":"5.0.1", "artifactId":"fb_bidding_kid_sdk"}
}

# AAR_INFO = {
#     "aligames_ngad_release_sdk-2.5.45.aar":{"version":"2.5.45", "artifactId":"aligames_ngad_release_sdk"},
#     "au4399-sdk-release-1.1.8.aar":{"version":"1.1.8", "artifactId":"au4399-sdk-release"},
#     "baidu_mobads_sdk-5.82.aar":{"version":"5.82", "artifactId":"baidu_mobads_sdk"},
#     "baidu_mobads_sdk-4399_1.1.8.aar":{"version":"4399_1.1.8", "artifactId":"baidu_mobads_sdk"},
#     "gdtsdk_tbs-4.90.960.aar":{"version":"4.90.960", "artifactId":"gdtsdk_tbs"},
#     "gdtsdk_union-4.90.960.aar":{"version":"4.90.960", "artifactId":"gdtsdk_union"},
#     "mintegral_alphab-9.10.4_china.aar":{"version":"9.10.4_china", "artifactId":"mintegral_alphab"},
#     "mintegral_alphab-4399_1.1.8.aar":{"version":"4399_1.1.8", "artifactId":"mintegral_alphab"},
#     "mintegral_appwall-9.10.4_china.aar":{"version":"9.10.4_china", "artifactId":"mintegral_appwall"},
#     "mintegral_appwallext-9.10.4_china.aar":{"version":"9.10.4_china", "artifactId":"mintegral_appwallext"},
#     "mintegral_chinacommon-4399_1.1.8.aar":{"version":"4399_1.1.8", "artifactId":"mintegral_chinacommon"},
#     "mintegral_chinacommon-9.10.4_china.aar":{"version":"9.10.4_china", "artifactId":"mintegral_chinacommon"},
#     "mintegral_interactiveads-9.10.4_china.aar":{"version":"9.10.4_china", "artifactId":"mintegral_interactiveads"},
#     "mintegral_interstitial-9.10.4_china.aar":{"version":"9.10.4_china", "artifactId":"mintegral_interstitial"},

#     "mintegral_interstitialvideo-4399_1.1.8.aar":{"version":"4399_1.1.8", "artifactId":"mintegral_interstitialvideo"},
#     "mintegral_interstitialvideo-9.10.4_china.aar":{"version":"9.10.4_china", "artifactId":"mintegral_interstitialvideo"},

#     "mintegral_mtgdownloads-4399_1.1.8.aar":{"version":"4399_1.1.8", "artifactId":"mintegral_mtgdownloads"},
#     "mintegral_mtgdownloads-9.10.4_china.aar":{"version":"9.10.4_china", "artifactId":"mintegral_mtgdownloads"},

#     "mintegral_mtgjscommon-4399_1.1.8.aar":{"version":"4399_1.1.8", "artifactId":"mintegral_mtgjscommon"},
#     "mintegral_mtgjscommon-9.10.4_china.aar":{"version":"9.10.4_china", "artifactId":"mintegral_mtgjscommon"},

#     "mintegral_mtgnative-9.10.4_china.aar":{"version":"9.10.4_china", "artifactId":"mintegral_mtgnative"},
#     "mintegral_nativeex-9.10.4_china.aar":{"version":"9.10.4_china", "artifactId":"mintegral_nativeex"},
#     "mintegral_offerwall-9.10.4_china.aar":{"version":"9.10.4_china", "artifactId":"mintegral_offerwall"},
    

#     "mintegral_playercommon-4399_1.1.8.aar":{"version":"4399_1.1.8", "artifactId":"mintegral_playercommon"},
#     "mintegral_playercommon-9.10.4_china.aar":{"version":"9.10.4_china", "artifactId":"mintegral_playercommon"},

#     "mintegral_reward-4399_1.1.8.aar":{"version":"4399_1.1.8", "artifactId":"mintegral_reward"},
#     "mintegral_reward-9.10.4_china.aar":{"version":"9.10.4_china", "artifactId":"mintegral_reward"},

#     "mintegral_videocommon-4399_1.1.8.aar":{"version":"4399_1.1.8", "artifactId":"mintegral_videocommon"},
#     "mintegral_videocommon-9.10.4_china.aar":{"version":"9.10.4_china", "artifactId":"mintegral_videocommon"},

#     "mintegral_videojs-4399_1.1.8.aar":{"version":"4399_1.1.8", "artifactId":"mintegral_videojs"},
#     "mintegral_videojs-9.10.4_china.aar":{"version":"9.10.4_china", "artifactId":"mintegral_videojs"},

#     "oneway-plugin-2.1.3.aar":{"version":"2.1.3", "artifactId":"oneway-plugin"},
#     "torch_game-adcore-1.4.1036.aar":{"version":"1.4.1036", "artifactId":"torch_game-adcore"},
#     "wssdk_ads-1.0.1.aar":{"version":"1.0.1", "artifactId":"wssdk_ads"}
# }