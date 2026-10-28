# UIKit 布局经验：contentLayoutGuide vs frameLayoutGuide

> 来源场景：0点输入法笔画面板符号条居中（2026-10-28 build38，用户实测确认）

## 一句话结论

**滚动视图内容要填满可视宽度 → 宽度绑 `frameLayoutGuide`；要按内容自然排布 → 才用 `contentLayoutGuide`。**

## 区别

- `contentLayoutGuide` = 内容区域（尺寸由内容内在宽度推断，可能小于可视区）
- `frameLayoutGuide` = 滚动视图可视区域（恒等于 bounds）

## 典型 bug

UIScrollView 内嵌 UIStackView，符号按钮宽度绑 `contentLayoutGuide.widthAnchor`：
- 结果：UIStackView 宽度 = 内容内在宽度（符号文字+按钮边距，约 30~40pt），内容贴左、右侧大片留白。
- 修复：宽度改绑 `frameLayoutGuide.widthAnchor`，删除原 trailing 约束 → 内容填满可视宽度，文字水平居中，且随动态宽度同步居中。
- 垂直方向仍用 `contentLayoutGuide.top/bottom`，滚动高度由内容推断。

## 完整案例

见 0point-ime 工程 `Docs/经验_contentLayoutGuide与frameLayoutGuide.md`。