class UserStorage {
    loginUser(id, password, onSuccess, onError) {
        // id, password를 서버로 전송하여 가입정보 인증
        setTimeout(() => {
            if ((id === 'java' && password === 'script') ||
                (id === 'call' && password === 'back')) {
                onSuccess(id);
            } else {
                onError(new Error('not found'));
            }
        }, 2000);
    }
    getRoles(id, onSuccess, onError) {
        // 로그인 성공 시 id를 서버로 전송하여 권한 확인
        setTimeout(() => {
            if (id === 'java') {
                onSuccess({ id: 'java', role: 'admin' });
            } else if (id === 'call') {
                onSuccess({ id: 'call', role: 'manager' });
            } else {
                onError(new Error('no access'));
            }
        }, 1000);
    }
}

const userStorage = new UserStorage();
const id = 'java';
const password = 'script';
// 단점
// 가독성 떨어짐 (구조가 복잡함)
const s = function(id) {
    userStorage.getRoles(id, (user) => {
        // 인증 성공
        // 사용자 권한 확인 - getRoles() 호출
        alert(`Hello ${user.id}, you have a ${user.role}`)
    }, (error) =>{
        // 사용자 권한 확인 실패
        console.log(error);
    })
}

userStorage.loginUser(id, password, s,function (id) {
    // 인증 성공
    // 사용자 권한 확인 - getRoles() 호출
    userStorage.getRoles(id, (user) => {
        alert(
            `Hello ${user.id}, you have a ${user.role}`)
    }, (error) => { // 사용자 권한 확인 실패
        console.log(error);
    })
}, function (error) {
    // 인증 실패
    console.log(error);
});