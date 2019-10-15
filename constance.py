#!/usr/bin/python 
# -*- coding: utf-8 -*-
'''
Created on 20191012

@author: shun
'''
MAVEN_CMD = "mvn install:install-file -DgroupId=%s -DartifactId=%s -Dversion=%s -Dpackaging=aar -Dfile=%s"

GROUP_ID = "com.taurusx.ads"

AAR_INFO = {
    "duadplatform_cw-1.2.2.aar":{"version":"1.2.2", "artifactId":"duadplatform_cw"},
    "duadplatform_hw-1.2.2.aar":{"version":"1.2.2", "artifactId":"duadplatform_hw"},
    "ia-mraid-kit-release-7.2.1.aar":{"version":"7.2.1", "artifactId":"ia-mraid-kit-release"},
    "ia-native-kit-release-7.2.1.aar":{"version":"7.2.1", "artifactId":"ia-native-kit-release"},
    "ia-sdk-core-release-7.2.1.aar":{"version":"7.2.1", "artifactId":"ia-sdk-core-release"},
    "ia-video-kit-release-7.2.1.aar":{"version":"7.2.1", "artifactId":"ia-video-kit-release"},
    "mopub-moat-mobile-app-kit-2.4.5.aar":{"version":"2.4.5", "artifactId":"mopub-moat-mobile-app-kit"},
    "mopub-sdk-interstitial-5.7.1.aar":{"version":"5.7.1", "artifactId":"mopub-sdk-interstitial"},
    "toutiao_open_ad_sdk-2.3.0.7.aar":{"version":"2.3.0.7", "artifactId":"toutiao_open_ad_sdk"},
    "criteopublishersdk-3.0.1.aar":{"version":"3.0.1", "artifactId":"criteopublishersdk"},
    "unity-ads-3.1.0.aar":{"version":"3.1.0", "artifactId":"unity-ads"}
}