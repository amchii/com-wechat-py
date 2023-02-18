import enum


class WechatMsgType(enum.IntEnum):
    文字 = 1
    图片 = 3
    语音 = 34
    好友确认 = 37
    名片 = 42
    视频 = 43
    表情 = 47
    位置 = 48
    共享实时位置_文件_转账_链接 = 49
    语音通话消息 = 50
    微信初始化 = 51
    语音通话通知 = 52
    语音通话邀请 = 53
    小视频 = 62
    SYS_NOTICE = 9999
    系统消息_红包 = 10000
    撤回_群语音邀请 = 10002
