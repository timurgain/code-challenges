describe('Global variable', () => {
  it('global variable should be defined', () => {
    expect(global.myGlobalVariable).toBe('Hello, World!');
  });
  it('global variable from .env should be defined', () => {
    expect(global.SECRET_TOKEN).toBeTruthy();
  });
})
