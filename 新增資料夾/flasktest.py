from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

WAYPOINTS = [
    {'id': 'A', 'name': '充电站',   'x': 150, 'y': 550},
    {'id': 'B', 'name': '原料仓库', 'x': 320, 'y': 180},
    {'id': 'C', 'name': '装配车间', 'x': 620, 'y': 350},
    {'id': 'D', 'name': '质检区',   'x': 800, 'y': 200},
    {'id': 'E', 'name': '出货口',   'x': 850, 'y': 580},
    {'id': 'F', 'name': '休息区',   'x': 480, 'y': 600},
]

@app.route('/')
def index():
    return render_template('index.html', waypoints=WAYPOINTS)

@app.route('/api/navigate', methods=['POST'])
def navigate():
    """前端按钮点击后，在这里操控实体机器人"""
    data = request.get_json()

    # ↓↓↓ 这里换成你的机器人 SDK 调用 ↓↓↓
    # 例如： robot.move_to(data['x'], data['y'])
    print(f"机器人前往: {data['name']} ({data['x']}, {data['y']})")

    return jsonify(success=True)

@app.route('/api/status')
def status():
    """返回机器人当前坐标（可选）"""
    # 从机器人读取真实位置
    # x, y = robot.get_position()
    return jsonify(x=500.0, y=400.0)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)