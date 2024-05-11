describe('custom matchers', () => {
  it('should check a range', () => {
    expect(100).toBeWithinRange(90, 110)
    expect(101).not.toBeWithinRange(90, 100)
  })
})
