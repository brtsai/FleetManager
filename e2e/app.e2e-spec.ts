import { FleetmanagerPage } from './app.po';

describe('fleetmanager App', function() {
  let page: FleetmanagerPage;

  beforeEach(() => {
    page = new FleetmanagerPage();
  });

  it('should display message saying app works', () => {
    page.navigateTo();
    expect(page.getParagraphText()).toEqual('app works!');
  });
});
